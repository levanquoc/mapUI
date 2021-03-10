##  OI from Data-package wroten by Nam-san ##
##  ASTI 05102020
##  Ver. 0.0.1



class Namespace(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


BAUD_RATE           = 9600          #Base on "Physical interface" in Data-package MCU and MCP from Nam-san

CONTROL_OP          = Namespace(
    CONTROL_SPEED           = (0X5B,0XA3),  #DATA content 4 bytes: 2 high bytes are normal speed, 2 low bytes are slow speed
    CONTROL_AGV             =(0x5B,0xA0)
)

INFO_OP             = Namespace(
    BASIC_BATTERY           = 3, #0x03
    BASIC_SPEED             = 4,#0x04
    ERROR_STATUS            = 8 #0x08

)

OPCODES             = Namespace(
    START_BYTE              = 238,#0xEE
    END_BYTE                = 170,#0xAA
    XOR_VALUE               = 65535, #0XFFFF
    START_BYTE_BATTERY      =221,#0xDD
    END_BYTE_BATTERY        =119#0x77

)

REQUEST             = Namespace(
    SPEED_INFO              = 0xA3,
    BATTERY_INFO            = (0XA5,0x03),
    BATTERY_VOTAGE          = (0XA5,0x04),
    HARDWARE_VERSION        = (0xA5,0x05),  
    ERR_STATUS              = (0xB5, 0x08),
    SPEED                   = (0xB5,0x04),
    LINESTATUS_AND_HALLINPUT= (0xB5,0x05),
    SEND_STEP               = (0x5B,0xA8),
    RFID_FEEDBACK           = (0xB5,0x06),
    READ_ERROR              = (0xB5,0x08),
    RESET_MCU               = (0xB5,0xA4)
)
SELECT_HEAD         ={"Front":0x00,"Back":0x01}
FUNCTION            ={"None":0x00,"Line":0X01,"Hook":0x02,"Position":0x03}
ROTATE_TYPE         ={"None":0x00, "Center":0x01,"Side":0x02}
COMMAND             ={"None":0x00,"Center":0x01,"Left":0x02,"Right":0x03}
LINE_TYPE           ={"One":0x00,"Fork Left":0x01,"Fork Right":0x02,"Cross":0x03}
SPEED_MAX           ={"Slow":0X01,"Normal":0X02,"High":0X03}
