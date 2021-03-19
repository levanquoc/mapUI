import serial
from struct import Struct
import struct
from OI import *
unpack_unsigned_byte = Struct('B').unpack
unpack_unsigned_2byte = Struct('H').unpack

class SerialCommandInterface(object):
    """
    This class handles sending commands to the Create2. Writes will take in tuples
    and format the data to transfer to the Create.
    """

    def __init__(self):
        """
        Constructor.
        Creates the serial port, but doesn't open it yet. Call open(port) to open
        it.
        """
        self.ser = serial.Serial()
        self.open( port='/dev/ttyUSB1', baud=9600, timeout=1)
        #self.open( port='/dev/ttyUSB0', baud=9600, timeout=1)


    def __del__(self):
        """
        Destructor.
        Closes the serial port
        """
        self.close()

    def open(self, port, baud, timeout):
        """
        Opens a serial port to the create.
        port: the serial port to open, ie, '/dev/ttyUSB0'
        buad: default is 115200, but can be changed to a lower rate via the create api
        """
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.timeout = 2
        # print self.ser.name
        if self.ser.is_open:
            self.ser.close()
        self.ser.open()
        if self.ser.is_open:
            # print("Create opened serial: {}".format(self.ser))
            print('-'*40)
            print(' Create opened serial connection')
            print('   port: {}'.format(self.ser.port))
            print('   datarate: {} bps'.format(self.ser.baudrate))
            print('-'*40)
        else:
            raise Exception('Failed to open {} at {}'.format(port, baud))


    def write(self, opcode, data=None):

        """
        Writes a command to the create. There needs to be an opcode and optionally
        data. Not all commands have data associated with it.

        opcode: see OI
        data: a tuple with data associated with a given opcode (see api)
        """
        if data:
            length_data = len(data)
        else:
            length_data = 0x00
        if type(opcode) == tuple:
            msg = (opcode[0],opcode[1],length_data,)
            msg_checksum=(opcode[1],length_data)
        else:
            msg = (opcode,length_data,)
        # Sometimes opcodes don't need data. Since we can't add
        # a None type to a tuple, we have to make this check.
        if data:
            msg += data

        Check_sum = self.calculateChecksum(msg_checksum)
        
        msg = (OPCODES.START_BYTE_BATTERY,) + msg

        

        msg = msg + Check_sum +  (OPCODES.END_BYTE_BATTERY,)

        print(">> write:", msg)
        self.ser.write(struct.pack('B' * len(msg), *msg))

    def checkStartEndByte(self, packet_byte_data):
        '''
        Check the start and end byte
        If true return true, otherwise flase
        '''
        len_pac = len(packet_byte_data)
        if len_pac==0:
            print("error:cannot get data from MCU")
            return False
        if Struct('B').unpack(packet_byte_data[0:1])[0] == OPCODES.START_BYTE_BATTERY:
            if Struct('B').unpack(packet_byte_data[len_pac-1:len_pac])[0] == OPCODES.END_BYTE_BATTERY:
                return True
            else:
                return False
        else:
            return False


    def checksumChecker(self, packet_byte_data):
        '''
        Calcualtor the check sum from start byte to data content byte and compare with checksum
        in position before end byte. If true return true, otherwise false
        '''
        len_pac = len(packet_byte_data)
        index = 2
        SUM = 0x00
        while index < len_pac -4:
            SUM += Struct('B').unpack(packet_byte_data[index:index+1])[0]
        
            #print(Struct('B').unpack(packet_byte_data[index:index+1])[0])
            index += 1
        Checker =(SUM ^ OPCODES.XOR_VALUE)+1
        #print(Checker)
        #print(Struct('>H').unpack(packet_byte_data[len_pac-3:len_pac-1])[0])
        if Checker == Struct('>H').unpack(packet_byte_data[len_pac-3:len_pac-1])[0]:
            return True
        else:
            return False        

    def read(self, num_bytes):
        """
        Read a string of 'num_bytes' bytes from the robot.
        Arguments:
            num_bytes: The number of bytes we expect to read.
        """
        if not self.ser.is_open:
            raise Exception('You must open the serial port first')

        data = self.ser.read(num_bytes)

        return data

    def close(self):
        """
        Closes the serial connection.
        """
        if self.ser.is_open:
            print('Closing port {} @ {}'.format(self.ser.port, self.ser.baudrate))
            self.ser.close()
    def calculateChecksum(self,data):
        data_out = 0
        for data in data:
            data_out += data
        data_out = data_out ^ OPCODES.XOR_VALUE
        data_out=data_out+1
        return struct.unpack('2B',(struct.pack('>1H',data_out)))
    def readBaterryInformation(self):
        self.write(REQUEST.BATTERY_INFO)
        packet_byte_data=self.read(num_bytes=34)     
        #print(packet_byte_data)
        #print("pack",len(packet_byte_data))
        #print(self.checksumChecker(packet_byte_data))
        #if self.checkStartEndByte(packet_byte_data) and self.checksumChecker(packet_byte_data):
        data_length=int(unpack_unsigned_byte(packet_byte_data[3:4])[0])
        #print("data_length",data_length)
        Total_voltage               = int(Struct('>H').unpack(packet_byte_data[4:6])[0])/100
        #print("total_vol",Total_voltage)
        Current                     = (65536-int((Struct('>H').unpack(packet_byte_data[6:8])[0])))/100
        The_remaining_capacity      = int(Struct('>H').unpack(packet_byte_data[8:10])[0])*10
        Nominal_capacity            =  int(Struct('>H').unpack(packet_byte_data[10:12])[0])*10
        Cycles                      = Struct('>H').unpack(packet_byte_data[12:14])[0]
        Production_Date             = Struct('>H').unpack(packet_byte_data[14:16])[0]
        Date                        =(Production_Date & 0x1f)
        Month                       =(Production_Date>>5)& 0x0f
        Year                        =2000+int((Production_Date>>9))
        InfoDate                    = str(Date) +"/"+str(Month)+"/"+str(Year)
        Equilibrium                 = Struct('>H').unpack(packet_byte_data[16:18])[0]
        Equilibrium_High            = Struct('>H').unpack(packet_byte_data[18:20])[0]
        Protection_status           =  Struct('>H').unpack(packet_byte_data[20:22])[0]
        Software_version            =  unpack_unsigned_byte(packet_byte_data[22:23])[0]
        RSOC                        =  unpack_unsigned_byte(packet_byte_data[23:24])[0]
        FET_control_status          =  unpack_unsigned_byte(packet_byte_data[24:25])[0]   
        Number_of_battery_strings   =  unpack_unsigned_byte(packet_byte_data[25:26])[0]
        Number_of_temperature_probes=  unpack_unsigned_byte(packet_byte_data[26:27])[0]
        The_first_temperature       = (int( Struct('>H').unpack(packet_byte_data[27:29])[0])-2731)/10
        The_second_temperature      =  (int( Struct('>H').unpack(packet_byte_data[29:31])[0])-2731)/10
        #The_third_temperature       =  unpack_unsigned_byte(packet_byte_data[31:33])[0]
        #The_fourth_temperature      =  unpack_unsigned_byte(packet_byte_data[33:35])[0]
        info=[Total_voltage,Current,The_remaining_capacity,Nominal_capacity,Cycles,Software_version,RSOC,FET_control_status,Number_of_battery_strings,Number_of_temperature_probes,The_first_temperature,The_second_temperature,0,0,InfoDate,Equilibrium,Equilibrium_High,Protection_status,]
        return info 
            

    def readBatteryCellVoltage(self):
        self.write(REQUEST.BATTERY_VOTAGE)
        packet_byte_data=self.read(num_bytes=50)
        if self.checkStartEndByte(packet_byte_data) and self.checksumChecker(packet_byte_data) :
            cell_pin=(int(unpack_unsigned_byte(packet_byte_data[3:4])[0]))/2
            cell_pin_voltage=[]
            for i in range(0,cell_pin):
                cell_pin_voltage[i]=unpack_unsigned_byte(packet_byte_data[i+4:i+6])[0]
                
        return cell_pin_voltage
        
    def readHardwareVersion(self):
        self.write(REQUEST.HARDWARE_VERSION)    
