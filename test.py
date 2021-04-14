from API import *

agv=AGV()

status,step,RSOC,distance,payload,speed=agv.read_status_AGV(1)
print(status,step,RSOC,distance,payload,speed)
    
    
