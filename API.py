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
                            # OPCODEs to process
#from JETSON.Serial_lib import SerialCommandInterface   # Serial module
from struct import Struct
#from JETSON.Packages import Data_packs_decoder
#from Deepstream.VisionAGV_API_v1 import changeAllowControlAGV
unpack_unsigned_byte = Struct('B').unpack  

class AGV(object):   
    def tohex(self,val, nbits):
        return hex((val + (1 << nbits)) % (1 << nbits))
    def pack_data_2bytes(self,data):
        data_pack=self.tohex(int(data),16)#convert string to hex
        data_pack=int(data_pack,0) #convert hex to int
        data_pack=struct.pack(">H",data_pack)
        return data_pack
    
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
                hex1=hex2=hex3=hex4=hex5=0x20
                #print(hex1,hex2,hex3,hex4,hex5)
   
            speed_max=SPEED_MAX[data[i][8]]    
            wait_time=self.pack_data_2bytes(data[i][9]) 
            bytes_one_wait_time     =wait_time[0]
            bytes_second_wait_time  =wait_time[1]
            data_opcode=(step,select_head,function,rotate_type,a,b,c,d,line_turn_command,line_type,hex1,hex2,hex3,hex4,hex5,hex6,hex7,hex8,speed_max,bytes_one_wait_time,bytes_second_wait_time)
            #data_opcode=(step,select_head,function,rotate_type,a,b,c,d,line_turn_command,line_type,speed_max,bytes_one_wait_time,bytes_second_wait_time)
            data_process.append(data_opcode)
        return data_process

            

            




          