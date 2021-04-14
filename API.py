# ASTI License

# This is main api for ASTI AGV

#######ASTI AGV#######
######################
# Author :  Son     ##
# Date:     02102020##
# Version:  0.0.1   ##
######################
import threading

import struct 
import pickle
from tkinter import messagebox
import binascii
import codecs                                 # to collect opcode into frame or unpack them.
import time                                     # IF need delay
from OI import *    
from createSerial import SerialCommandInterface
# OPCODEs to process
#from JETSON.Serial_lib import SerialCommandInterface   # Serial module
from struct import Struct
#from JETSON.Packages import Data_packs_decoder
#from Deepstream.VisionAGV_API_v1 import changeAllowControlAGV
unpack_unsigned_byte = Struct('B').unpack  

class AGV(object):
    def __init__(self, baud=BAUD_RATE):
        '''
        Setup for class
        - check for port
        - creates serial port
        - create decoder
        '''
        
        self.SCI     = SerialCommandInterface()
        self.port    = self.SCI.Check_TTLUART_module()
        #self.SCI.open("COM3",115200,2)
        self.decoder = None
        self.visionService = None
        
        
    def __del__(self):
        '''Clean everything before leaving'''
        pass
    def Check_STARTnEND_BYTE(self, packet_byte_data):
        '''
        Check the start and end byte
        If true return true, otherwise flase
        '''
        len_pac = len(packet_byte_data)
        if len_pac==0:
            print("error:cannot get data from MCU")
            return False
        if Struct('B').unpack(packet_byte_data[0:1])[0] == OPCODES.START_BYTE:
            if Struct('B').unpack(packet_byte_data[len_pac-1:len_pac])[0] == OPCODES.END_BYTE:
                return True
            else:
                return False
        else:
            return False    
    def Checksum_checker(self, packet_byte_data):
        '''
        Calcualtor the check sum from start byte to data content byte and compare with checksum
        in position before end byte. If true return true, otherwise false
        '''
        len_pac = len(packet_byte_data)
        index = 1
        SUM = 0x00
        while index < len_pac -3 :
            SUM += Struct('B').unpack(packet_byte_data[index:index+1])[0]
        
            #print(Struct('B').unpack(packet_byte_data[index:index+1])[0])
            index += 1
        Checker = SUM ^ OPCODES.XOR_VALUE
        
        #print(Struct('>H').unpack(packet_byte_data[len_pac-3:len_pac-1])[0])
        if Checker == Struct('>H').unpack(packet_byte_data[len_pac-3:len_pac-1])[0]:
            return True
        else:
            return False
    def Cal_Checksum(self, datas):
        data_out = 0
        for data in datas:
            data_out += data
        data_out = data_out ^ OPCODES.XOR_VALUE
        return struct.unpack('2B',(struct.pack('>1H',data_out)))   
    def tohex(self,val, nbits):
        return hex((val + (1 << nbits)) % (1 << nbits))
    def pack_data_2bytes(self,data):
        data_pack=self.tohex(int(data),16)#convert string to hex
        data_pack=int(data_pack,0) #convert hex to int
        data_pack=struct.pack(">H",data_pack)
        return data_pack
   
    
    def read_status_AGV(self,ids):
        
        self.SCI.write(ids,REQUEST.STATUS,data=None)
        packet_byte_data=self.SCI.read(16)
        if self.Check_STARTnEND_BYTE(packet_byte_data) and self.Checksum_checker(packet_byte_data) and unpack_unsigned_byte(packet_byte_data[3:4])[0]==0x00:
            status=unpack_unsigned_byte(packet_byte_data[5:6])[0]
            step=unpack_unsigned_byte(packet_byte_data[6:7])[0]
            RSOC=unpack_unsigned_byte(packet_byte_data[7:8])[0]
            distance=Struct('>H').unpack(packet_byte_data[8:10])[0]
            payload=unpack_unsigned_byte(packet_byte_data[10:11])[0]
            speed=Struct('>H').unpack(packet_byte_data[11:13])[0]
        else:
            status=distance=step=speed=RSOC=payload=False
        return status,step,distance,speed,RSOC,payload    
            
    def start_AGV(self,ids):
        self.SCI.write(ids,CONTROL_OP.CONTROL_AGV,data=(0x01,))
        packet_byte_data=self.SCI.read(8)
        print(packet_byte_data)
        if self.Check_STARTnEND_BYTE(packet_byte_data) and self.Checksum_checker(packet_byte_data) and unpack_unsigned_byte(packet_byte_data[3:4])[0]==0x00:
            return True
        return False
    def stop_AGV(self,ids):
        self.SCI.write(ids,CONTROL_OP.CONTROL_AGV,data=0x00)
        packet_byte_data=self.SCI.read(8)
        print(packet_byte_data)
        if self.Check_STARTnEND_BYTE(packet_byte_data) and self.Checksum_checker(packet_byte_data) and unpack_unsigned_byte(packet_byte_data[3:4])[0]==0x00:
            return True
        return False
    def send_speed(self,ids,highSpeed,normalSpeed,lowSpeed):
        data_speed = struct.unpack('6B', struct.pack('>3h',highSpeed,normalSpeed,lowSpeed))
        self.SCI.write(ids,CONTROL_OP.CONTROL_SPEED, data = data_speed)
        packet_byte_data=self.SCI.read(8)
        if self.Check_STARTnEND_BYTE(packet_byte_data) and self.Checksum_checker(packet_byte_data) and unpack_unsigned_byte(packet_byte_data[3:4])[0]==0x00:
            return True
        return False    
        
        
        
    def send_step(self,ids,data):
        self.SCI.write(ids,REQUEST.SEND_STEP,data)
        packet_byte_data=self.SCI.read(8)
        print(packet_byte_data)
        if self.Check_STARTnEND_BYTE(packet_byte_data) and self.Checksum_checker(packet_byte_data) and unpack_unsigned_byte(packet_byte_data[3:4])[0]==0x00:
            return True
        return False 
    def Check_STARTnEND_BYTE(self, packet_byte_data):

        len_pac = len(packet_byte_data)
        if len_pac==0:
            print("error:cannot get data from MCU")
            return False
        if Struct('B').unpack(packet_byte_data[0:1])[0] == OPCODES.START_BYTE:
            if Struct('B').unpack(packet_byte_data[len_pac-1:len_pac])[0] == OPCODES.END_BYTE:
                return True
            else:
                return False
        else:
            return False        
    def process_step_data(self,data):
        data_process=[]
        for i in range(0,len(data)):

            step=self.tohex(int(i)+1,8)
            step=int(step,0)
            #print(step)
            select_head=SELECT_HEAD[data[i][0]]
            #print(select_head)
            function=FUNCTION[data[i][1]]
            rotate_type=ROTATE_TYPE[data[i][2]]
            distance=self.pack_data_2bytes(data[i][3])
            a=distance[0]
            b=distance[1]
            degree_rotate=self.pack_data_2bytes(data[i][4])
            c=degree_rotate[0]
            d=degree_rotate[1]
            line_turn_command=COMMAND[data[i][5]]
            line_type=LINE_TYPE[data[i][6]]
            
            RFID_data=data[i][7]
            if(len(RFID_data)==8):
                hex1=hex(ord(RFID_data[0]))
                hex1=int(hex1,0)
                hex2=hex(ord(RFID_data[1]))
                hex2=int(hex2,0)
                hex3=hex(ord(RFID_data[2]))
                hex3=int(hex3,0)
                hex4=hex(ord(RFID_data[3]))
                hex4=int(hex4,0)
                hex5=hex(ord(RFID_data[4]))
                hex5=int(hex5,0)
                hex6=hex(ord(RFID_data[5]))
                hex6=int(hex6,0)
                hex7=hex(ord(RFID_data[6]))
                hex7=int(hex7,0)
                hex8=hex(ord(RFID_data[7]))
                hex8=int(hex8,0)
                #print(hex1,hex2,hex3,hex4,hex5)
            else:
                hex1=hex2=hex3=hex4=hex5=hex6=hex7=hex8=0x20
                #print(hex1,hex2,hex3,hex4,hex5)
   
            speed_max=SPEED_MAX[data[i][8]]    
            wait_time=self.pack_data_2bytes(data[i][9]) 
            bytes_one_wait_time     =wait_time[0]
            bytes_second_wait_time  =wait_time[1]
            data_opcode=(step,select_head,function,rotate_type,c,d,line_turn_command,line_type,hex1,hex2,hex3,hex4,hex5,hex6,hex7,hex8,speed_max,a,b,bytes_one_wait_time,bytes_second_wait_time)
            #data_opcode=(step,select_head,function,rotate_type,a,b,c,d,line_turn_command,line_type,speed_max,bytes_one_wait_time,bytes_second_wait_time)
            data_process.append(data_opcode)
        return data_process

            

            




          