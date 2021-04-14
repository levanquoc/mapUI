from values import *
import numpy as np 
import collections
import sys
from tkinter import *
from tkinter import messagebox 
from Line import *
from RFID import *
from copy import copy, deepcopy
from API import *
from createSerial import *
import json 
import tkinter.filedialog
import ast
import libtcodpy as libtcod
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import numpy as np
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        #print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom    
def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level,agv, root#,serial
    w = gui
    top_level = top
    agv=AGV()
    #serial=SerialCommandInterface()
    root = top
    root.geometry(windown_size)

    w.mapFrame.bind('<Configure>', create_grid)

    global labelsRFID,labelsLine,lines,pickingHolder,step,RFIDstep,grid_coor,matrix,data,labelsLinehorizontal,labelsLinevertical,labelsLinecross
    labelsRFID=[]
    labelsLine=[]
    holderItem = []
    labelsLinehorizontal=[]
    labelsLinevertical=[]
    labelsLinecross=[]
    step=[]
    app=FullScreenApp(root)
    lines = []
    RFIDstep=[]  
    grid_coor=[]
    data=[]
    
    #matrix=np.zeros((10,10),int)
    #matrix=matrix.tolist()
def create_grid(event=None):
    w1 = w.mapFrame.winfo_width() # Get current width of canvas
    h1 = w.mapFrame.winfo_height() # Get current height of canvas
    w.mapFrame.delete('grid_line') # Will only remove the grid_line

    global x_info2,y_info2, y_info, x_info
    x_info = []
    y_info = []             
    x_info2 = []
    y_info2 = []
    # Creates all vertical lines at intevals of 100
    for i in range(0, w1, grid_size*2):
        x_info.append(i-grid_size)
        w.mapFrame.create_line([(i, 0), (i, h1)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h1, grid_size*2):
        y_info.append(i-grid_size)
        w.mapFrame.create_line([(0, i), (w1, i)], tag='grid_line')
    
    for i in x_info:
        for j in y_info:
                python_green = "#FFFFFF"
                x1, y1 = (i - 1), (j - 1)
                x2, y2 = (i + 1), (j + 1)               
                x_info2.append(i-grid_size)
                y_info2.append(j-grid_size)
                grid_coor.append((i-grid_size,j-grid_size))
    
def createLinehorizontal():
    length=int(w.lenlineEntry.get())
    function=w.functionEntry.get()
    line_type=w.linetypeEntry.get()
    rotate_type=w.rotatetypeEntry.get()
    degree_rote=w.degreeroteEntry.get()
    speed_max=w.speedmaxEntry.get()
    wait_time=w.waittimeEntry.get()        
    f = Frame(w.mapFrame, height=LineHorizal['height'], width=length*LineHorizal['width'], bg="black")
    labelsLine.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    labelsLinehorizontal.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    f.pack_propagate(0) # don't shrink
    f.place(x = 0, y = 0)
    f.bind("<Button-1>",drag_start)
    f.bind("<B1-Motion>",drag_motion)
    f.bind("<ButtonRelease-1>",drop_motionHorizontal)
    f.bind("<Button-3>",popup)
    f.bind("<Enter>",information)  
def createLinevertical():  
    length=int(w.lenlineEntry.get())
    function=w.functionEntry.get()
    line_type=w.linetypeEntry.get()
    rotate_type=w.rotatetypeEntry.get()
    degree_rote=w.degreeroteEntry.get()
    speed_max=w.speedmaxEntry.get()
    wait_time=w.waittimeEntry.get()    
    f = Frame(w.mapFrame, height=length*LineVertical['height'], width=LineVertical['width'], bg="black")
    labelsLine.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    labelsLinevertical.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    f.pack_propagate(0) # don't shrink
    f.place(x = 0, y = 0)
    f.bind("<Button-1>",drag_start)
    f.bind("<B1-Motion>",drag_motion)
    f.bind("<ButtonRelease-1>",drop_motionVertical)
    f.bind("<Button-3>",popup)
    f.bind("<Enter>",information)    
def crossroadLine():
    length=int(w.lenlineEntry.get())
    function=w.functionEntry.get()
    line_type=w.linetypeEntry.get()
    rotate_type=w.rotatetypeEntry.get()
    degree_rote=w.degreeroteEntry.get()    
    speed_max=w.speedmaxEntry.get()
    wait_time=w.waittimeEntry.get()
    f = Frame(w.mapFrame, height=grid_size*2, width=grid_size*2, bg="#d9d9d9")
    k=Frame(f, height=LineVertical['height'], width=LineVertical['width'], bg="black")
    j = Frame(f, height=LineHorizal['height'], width=LineHorizal['width'], bg="black")
    k.place(x=grid_size/2+4, y = 0)
    j.place(y=grid_size/2+4, x = 0)
    f.pack_propagate(0) # don't shrink    
    f.place(x = 0, y = 0)
    labelsLine.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    labelsLinecross.append(Line(f,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time))
    f.bind("<Button-1>",drag_start)
    f.bind("<B1-Motion>",drag_motion)
    f.bind("<ButtonRelease-1>",drop_motion)
    f.bind("<Button-3>",popup)
    f.bind("<Enter>",information) 
def createRFID():
    try:
        index=int(w.indexCardEntry.get())
    except:
        messagebox.showerror(title="Error", message="Index is not valid")
        return 
    if index>len(labelsRFID)+1:
        messagebox.showerror(title="Error", message="Index is incorrect")
        return
    nameRFID=w.nameRFIDEntry.get()
    
    
    if len(w.nameRFIDEntry.get())!=0 and  len(w.nameRFIDEntry.get())!=8:
        messagebox.showerror(title="Error", message="Name RFID not valid")
        return    
    
    f = Frame(w.mapFrame, height=RFIDSize['height'], width=RFIDSize['width'], bg="blue")
    labelsRFID.append(RFID(index,f,nameRFID))
    f.pack_propagate(0) # don't shrink
    f.place(x = 0, y = 0)
    f.bind("<Button-1>",drag_start)
    f.bind("<B1-Motion>",drag_motion)
    f.bind("<ButtonRelease-1>",drop_motion)
    f.bind("<Button-3>",popup)  
    f.bind("<Enter>",informationRFID)
def calculateNewCoor(x):
    newGrid = grid_size/2
    newGrid2 = newGrid*2
    if(x%newGrid2 > newGrid):
        if((x%newGrid2-newGrid)>=(newGrid2-x%newGrid2)):
            x = ((int(x/newGrid2)+1)*newGrid2)
        else:
            x = ((int(x/newGrid2))*newGrid2+newGrid)
    else:
        if((newGrid-(x%newGrid2))>=(x%newGrid2)):
            x = ((int(x/newGrid2))*newGrid2)
        else:
            x = ((int(x/newGrid2))*newGrid2+newGrid)
    return x
    
def drop_motionHorizontal(event):
    widget = event.widget
    x = widget.winfo_x()  + event.x
    y = widget.winfo_y()  + event.y
    x = calculateNewCoor(x)             
    y = calculateNewCoor(y)             
    widget.place(x=find_nearest(x_info2, x),y=find_nearest(y_info, y)-int(grid_size/4))
    
def drop_motionVertical(event):
    widget = event.widget
    x = widget.winfo_x()  + event.x
    y = widget.winfo_y()  + event.y
    x = calculateNewCoor(x)             
    y = calculateNewCoor(y)
    widget.place(x=find_nearest(x_info, x)-int(grid_size/4),y=find_nearest(y_info2, y))
    
def refreshItem():    
    for item in labelsRFID:
        item.config(height=RFIDSize['height'], width=RFIDSize['width'])
        x = calculateNewCoor(item.winfo_x())       
        y = calculateNewCoor(item.winfo_y())       
        item.place(x=find_nearest(x_info2, x),y=find_nearest(y_info2, y))     
    for item in labelsLinehorizontal:
        item.config(height=LineHorizal['height'], width=LineHorizal['width'])
        x = calculateNewCoor(item.winfo_x())       
        y = calculateNewCoor(item.winfo_y())       
        item.place(x=find_nearest(x_info2, x),y=find_nearest(y_info, y)-int(grid_size/4))
    for item in labelsLinevertical:
        item.config(height=LineVertical['height'], width=LineVertical['width'])
        x = calculateNewCoor(item.winfo_x())       
        y = calculateNewCoor(item.winfo_y())       
        item.place(x=find_nearest(x_info, x)-int(grid_size/4),y=find_nearest(y_info2, y))
def information(event):
    widget=event.widget
    for i in range(0,len(labelsLine)):
        if widget==labelsLine[i].getId():            
            lenLine=labelsLine[i].getLength()
            function=labelsLine[i].getFunction()  
            line_type=labelsLine[i].getLinetype()
            rotate_type=labelsLine[i].getRotatetype()
            degree_rote=labelsLine[i].getDegreerote()            
            speed_max=labelsLine[i].getSpeedmax()
            wait_time=labelsLine[i].getWaittime()            
            w.lenlineEntry.delete(0,END)
            w.lenlineEntry.insert(0,lenLine)
            w.degreeroteEntry.delete(0,END)
            w.degreeroteEntry.insert(0,degree_rote)
            w.waittimeEntry.delete(0,END)
            w.waittimeEntry.insert(0,wait_time)
            for j,item in enumerate(w.functionEntry["values"]):
                if(item==function):
                    w.functionEntry.current(j) 

            for j,item in enumerate(w.linetypeEntry["values"]):
                if(item==line_type):
                    w.linetypeEntry.current(j)         
            for j,item in enumerate(w.rotatetypeEntry["values"]):
                if(item==rotate_type):
                    w.rotatetypeEntry.current(j)                           
            for j,item in enumerate(w.speedmaxEntry["values"]):
                if(item==speed_max):
                    w.speedmaxEntry.current(j)   

def informationRFID(event):
    widget=event.widget
    for i in range(0,len(labelsRFID)):
        if widget==labelsRFID[i].getId():
            index=labelsRFID[i].getStep()
            name=labelsRFID[i].getName()
            w.indexCardEntry.delete(0,END)
            w.indexCardEntry.insert(0,index)
            w.nameRFIDEntry.delete(0,END)
            w.nameRFIDEntry.insert(0,name)
               
def zoomIn():    
    global grid_size, LineHorizal, LineVertical, RFIDSize
    grid_size = grid_size + 2
    LineHorizal = {'height' : grid_size/2, 'width' : grid_size*2}
    LineVertical = {'height' : grid_size*2, 'width' : grid_size/2}
    RFIDSize = {'height' : grid_size*2, 'width' : grid_size*2}
    create_grid()
    refreshItem()
def zoomOut():   
    global grid_size, LineHorizal, LineVertical, RFIDSize
    grid_size = grid_size - 2
    LineHorizal = {'height' : grid_size/2, 'width' : grid_size*2}
    LineVertical = {'height' : grid_size*2, 'width' : grid_size/2}
    RFIDSize = {'height' : grid_size*2, 'width' : grid_size*2}
    create_grid()
    refreshItem()
def mBtnIncrease():
    if(pickingHolder.winfo_width()>pickingHolder.winfo_height()):
        pickingHolder.config(width=pickingHolder.winfo_width() + LineHorizal['width'])
    else:
        pickingHolder.config(height=pickingHolder.winfo_height() + LineVertical['height'])
def mBtndecrease():
    if(pickingHolder.winfo_width()>pickingHolder.winfo_height()):
        pickingHolder.config(width=pickingHolder.winfo_width() - LineHorizal['width'])
    else:
        pickingHolder.config(height=pickingHolder.winfo_height() - LineVertical['height'])
def loadDesign():
    '''         
    f = Frame(w.mapFrame, height=5*LineVertical['height'], width=LineVertical['width'], bg="black")
    labelsLine.append(Line(f,5,"head","head","head","High","Gead"))
    f.pack_propagate(0) # don't shrink
    f.place(x = 42, y = 30)
    f.bind("<Button-1>",drag_start)
    f.bind("<B1-Motion>",drag_motion)
    f.bind("<ButtonRelease-1>",drop_motionVertical)
    f.bind("<Button-3>",popup)
    f.bind("<Enter>",information) 
    '''    
    filename = tkinter.filedialog.askopenfilename(parent=root)
    file = open(filename)
    #init(top_level,w)
    #f.read()
    global labelsRFID
    for line in file:
        a=ast.literal_eval(line)
        if(a["name"]=="RFID"):
            f = Frame(w.mapFrame, height=RFIDSize['height'], width=RFIDSize['width'], bg="blue")
            labelsRFID.append(RFID(a["step"],f,a["nameRFID"]))
            f.pack_propagate(0) # don't shrink
            f.place(x = a["x"], y = a["y"])
            f.bind("<Button-1>",drag_start)
            f.bind("<B1-Motion>",drag_motion)
            f.bind("<ButtonRelease-1>",drop_motion)
            f.bind("<Button-3>",popup)  
            f.bind("<Enter>",informationRFID)
        if(a["name"]=="LineHorizal"):
            f = Frame(w.mapFrame, height=LineHorizal['height'], width=a["length"]*LineHorizal['width'], bg="black")
            labelsLine.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            labelsLinehorizontal.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            f.pack_propagate(0) # don't shrink
            f.place(x = a["x"], y =a["y"])
            f.bind("<Button-1>",drag_start)
            f.bind("<B1-Motion>",drag_motion)
            f.bind("<ButtonRelease-1>",drop_motionHorizontal)
            f.bind("<Button-3>",popup)
            f.bind("<Enter>",information) 
        if(a["name"]=="Linevertical"):
            f = Frame(w.mapFrame, height=a["length"]*LineVertical['height'], width=LineVertical['width'], bg="black")
            labelsLine.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            labelsLinevertical.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            f.pack_propagate(0) # don't shrink
            f.place(x = a["x"], y =a["y"])
            f.bind("<Button-1>",drag_start)
            f.bind("<B1-Motion>",drag_motion)
            f.bind("<ButtonRelease-1>",drop_motionHorizontal)
            f.bind("<Button-3>",popup)
            f.bind("<Enter>",information)  
        if(a["name"]=="LineCross"):
            f = Frame(w.mapFrame, height=grid_size*2, width=grid_size*2, bg="#d9d9d9")
            k=Frame(f, height=LineVertical['height'], width=LineVertical['width'], bg="black")
            j = Frame(f, height=LineHorizal['height'], width=LineHorizal['width'], bg="black")
            k.place(x=grid_size/2+4, y = 0)
            j.place(y=grid_size/2+4, x = 0)
   
            labelsLine.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            labelsLinecross.append(Line(f,a["length"],a["function"],a["line_type"],a["rotate_type"],a["degree_rote"],a["speed_max"],a["wait_time"]))
            
            f.pack_propagate(0) # don't shrink
            f.place(x = a["x"], y =a["y"])
            f.bind("<Button-1>",drag_start)
            f.bind("<B1-Motion>",drag_motion)
            f.bind("<ButtonRelease-1>",drop_motionHorizontal)
            f.bind("<Button-3>",popup)
            f.bind("<Enter>",information) 
           
def saveDesign(): 
    #print(len(labelsLinehorizontal))
    #print(len(labelsLinevertical))
    f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return    
    if len(labelsLinehorizontal)>0:
    
        for i in range(0,len(labelsLinehorizontal)):
            try:
                ids        = labelsLinehorizontal[i].getId()
                length     = labelsLinehorizontal[i].getLength()
                function   = labelsLinehorizontal[i].getFunction()
                line_type  = labelsLinehorizontal[i].getLinetype()
                rotate_type= labelsLinehorizontal[i].getRotatetype()
                degree_rote= labelsLinehorizontal[i].getDegreerote()
                speed_max  = labelsLinehorizontal[i].getSpeedmax()
                wait_time  = labelsLinehorizontal[i].getWaittime()
                x          = ids.winfo_x()
                y          = ids.winfo_y()
                dict={"name":"LineHorizal","f":str(ids),"length":length,"function":function,"line_type":line_type,"degree_rote":degree_rote,"rotate_type":rotate_type,"speed_max":speed_max,"wait_time":wait_time,"x":x,"y":y}
                f.write( str(dict)+"\n")
            except Exception as e:
                pass
    if len(labelsLinecross)>0:
        for i in range(0,len(labelsLinecross)):
            try:
                ids        = labelsLinecross[i].getId()
                length     = labelsLinecross[i].getLength()
                function   = labelsLinecross[i].getFunction()
                line_type  = labelsLinecross[i].getLinetype()
                rotate_type= labelsLinecross[i].getRotatetype()
                degree_rote= labelsLinecross[i].getDegreerote()
                speed_max  = labelsLinecross[i].getSpeedmax()
                wait_time  = labelsLinecross[i].getWaittime()
                x          = ids.winfo_x()
                y          = ids.winfo_y()
                dict={"name":"LineCross","f":str(ids),"length":length,"function":function,"line_type":line_type,"degree_rote":degree_rote,"rotate_type":rotate_type,"speed_max":speed_max,"wait_time":wait_time,"x":x,"y":y}
                f.write( str(dict)+"\n") 
            except :
                pass
    if len(labelsLinevertical)>0:    
        for i in range(0,len(labelsLinevertical)):
            try:
                ids        = labelsLinevertical[i].getId()
                length     = labelsLinevertical[i].getLength()
                function   = labelsLinevertical[i].getFunction()
                line_type  = labelsLinevertical[i].getLinetype()
                rotate_type= labelsLinevertical[i].getRotatetype()
                degree_rote= labelsLinevertical[i].getDegreerote()
                speed_max  = labelsLinevertical[i].getSpeedmax()
                wait_time  = labelsLinevertical[i].getWaittime()
                x          = ids.winfo_x()
                y          = ids.winfo_y()
                dict={"name":"Linevertical","f":str(ids),"length":length,"function":function,"line_type":line_type,"degree_rote":degree_rote,"rotate_type":rotate_type,"speed_max":speed_max,"wait_time":wait_time,"x":x,"y":y}  
                f.write( str(dict)+"\n")
            except:
                pass
    if len(labelsRFID)>0:            
        for i in range(0,len(labelsRFID)):
            try:
                step       = labelsRFID[i].getStep()
                ids        = labelsRFID[i].getId()            
                name       = labelsRFID[i].getName()
                x          = ids.winfo_x()
                y          = ids.winfo_y()
                dict={"name":"RFID","f":str(ids),"step":step,"nameRFID":name,"x":x,"y":y} 
                f.write( str(dict)+"\n")
            except :
                pass

    f.close()
def newDesign():
    print('main_support.newDesign')    
def downLine():
    if(pickingHolder.winfo_width()>pickingHolder.winfo_height()):
        pickingHolder.config(width=pickingHolder.winfo_height(),height=pickingHolder.winfo_width())
        pickingHolder.bind("<ButtonRelease-1>",drop_motionVertical)            
def leftLine():
    if(pickingHolder.winfo_width()<pickingHolder.winfo_height()):
    
        pickingHolder.config(width=pickingHolder.winfo_height(),height=pickingHolder.winfo_width())

def rightLine():
    if(pickingHolder.winfo_width()<pickingHolder.winfo_height()):
        pickingHolder.config(width=pickingHolder.winfo_height(),height=pickingHolder.winfo_width())
    

def upLine():
    if(pickingHolder.winfo_width()>pickingHolder.winfo_height()):
        pickingHolder.config(width=pickingHolder.winfo_height(),height=pickingHolder.winfo_width())

def lengLine():
    lenLine=w.lenLineghtEntry.get()
    if(pickingHolder.winfo_width()>pickingHolder.winfo_height()):
        pickingHolder.config(width= int(lenLine)*LineHorizal['width'])
    else:
        pickingHolder.config(height= int(lenLine)*LineVertical['height'])



def view():
    global step
    for i in range(0,len(step)):
        print(step[i].getCommand())
    for i in range(0,len(RFIDstep)):
        print(RFIDstep[i].getName())
def reset():
    global step,data
    step=[]
    data=[]
    messagebox.showinfo(title="Information", message="Done") 

def copy_object(obj):
    new_object=[]
    for item in obj:
        new_object.append(copy(item))
    return new_object
def startAGV():
    try:
        nameAGV=(int(w.nameAgvEntry.get()))
        if(agv.start_AGV(nameAGV)):
            messagebox.showinfo(title="",message="Succsess")
        else:
            messagebox.showerror(title="Error",message="Communication error")
            
    except:
        messagebox.showerror(title="Error",message="AGV's name is not correct")
def stopAGV():
    try:
        nameAGV=(int(w.nameAgvEntry.get()))
        if(agv.stop_AGV(nameAGV)):
            messagebox.showinfo(title="",message="Succsess")
        else:
            messagebox.showerror(title="Error",message="Communication error")
            
    except:
        messagebox.showerror(title="Error",message="AGV's name is not correct")
        
def checkStatus():
    try:
        nameAGV=(int(w.nameAgvEntry.get()))
    except:
        messagebox.showerror(title="Error",message="AGV's name is not correct")   
        return     
    status,step,RSOC,distance,payload,speed=agv.read_status_AGV(nameAGV)
    if(status==0xFF):
        statusAGV="Error"
    if(status==0):
        statusAGV="Stop"
    if(status==1):
        statusAGV="Start"
    distance=distance/100
    if(payload==0):
        payloadStatus="AGV has no load"
    if(payload==1):
        payloadStatus="AGV has load"    
    messagebox.showinfo(title="Status",message="Current state :"+statusAGV+"\n""Step state: "+str(step)+"\n""Distance AGV has traveled:"+str(distance)+" (m)\n""Speed :"+str(speed/1000)+" (m/s)\n"+payloadStatus+"\n""Batery percent: "+str(RSOC)+" %\n")
   
            

def setupStep():
    
    global RFIDstep,matrix,step
    RFIDstep=[]
    nameRFID=[]
    pathRFID=[]
    pathRFID_Item=[]
    pathLine=[]
    pathLine_Item=[]
    command=[]
    line_type=[]
    lenLine=[]
    degree_rote=[]
    wait_time=[]
    speed_max=[]
    function=[]
    head=[]
    rotate_type=[]   
    ids=[]   
    #messagebox.showinfo(title="Information", message="Done")         
    matrix=np.zeros((len(y_info),len(x_info)),int) #create matrix 0
    matrix=matrix.tolist()
    matrix= create_matrix_map(matrix,labelsRFID,labelsLine) #create map 
    try:
        start=int(w.startEntry.get())#point start
        end=int(w.endEntry.get())#point end
    except:
        messagebox.showerror("ERROR","Incorrect starting point or end point, please re-enter")
        return 
    head_select=w.headEntry.get()
    if head_select=="":
        messagebox.showerror("Error","The head function is not selected")
        return 
    matrix,pathRFID,pathLine,x_start,y_start=make_pointstart_and_pointend(matrix,labelsRFID,labelsLine,pathRFID,pathLine,start,end) #make point
    path=bfs(matrix,(x_start,y_start)) 
    if path==None:# shortest parth'
        messagebox.showerror("Error","Route not found")
        return        
    pathRFID_Item,pathLine_Item=find__item_path(path,pathRFID,pathLine,pathRFID_Item,pathLine_Item)
    
    command=make_command(pathRFID_Item,pathLine_Item,command)
    nameRFID,_=find_RFIDname_in_route(pathRFID_Item,labelsRFID)
    ids,head,lenLine,function,line_type,rotate_type,degree_rote,wait_time,speed_max=status_line_in_route(pathLine_Item,labelsLine,ids,head,lenLine,function,line_type,rotate_type,degree_rote,wait_time,speed_max,head_select)#status line
            
    status_line=change_type_line(matrix,labelsRFID,labelsLine,command,line_type,head,pathLine_Item,pathRFID_Item)
    
    
    for i in range(0,len(pathLine_Item)):
        data.append([ids[i],head[i],function[i],rotate_type[i],lenLine[i],degree_rote[i],command[i],status_line[i],nameRFID[i+1],speed_max[i],wait_time[i]])
    
    #print(data)
    '''
    for i in range(0,len(data)):
        step=agv.process_step_data(data)    
    
    for i in range(0,len(command)):
        print(head[i],function[i],rotate_type[i],degree_rote[i],command[i],status_line[i],nameRFID[i],speed_max[i],lenLine[i],wait_time[i]) 
    ''' 
def send():
    try:
        nameAGV=int(w.nameAGV.get())
    except:
        messagebox.showerror(title="Error",message="AGV's name is not correct")
        return        
    dem=0
    count=0

    if len(data)>0:
        for j in range (0,len(labelsLine)):
            
            for i in range (0,len(data)):
                if(labelsLine[j].getId()==data[i][0] and labelsLine[j].getFunction()=="Hook"):
                    print(type(data[i][2]))
                    count=count+1
                    if count%2==0:
                        data[i][2]="Line"   
            count=0        
                   
        for i in range(0,len(data)):
            step=agv.process_step_data(data)  
            print(data[i][2])
        for i in range(0,len(step)):
            libtcod.console_check_for_keypress()
            if(agv.send_step(nameAGV,step[i])):
                dem=dem+1
        if(dem==len(step)):        
            messagebox.showinfo(title="Information", message="Done") 
        else:
            messagebox.showerror(title="Error", message="Communication error")     
    else:
        messagebox.showinfo(title="Information", message="Route not found")

          
    def make_step(pathLine_Item,head,function,rotate_type,lenLine,degree_rote,command,status_line,nameRFID,speed_max,wait_time,data,step) :       
        for i in range(0,len(pathLine_Item)):
            data.append((head[i],function[i],rotate_type[i],lenLine[i],degree_rote[i],command[i],status_line[i],nameRFID[i+1],speed_max[i],wait_time[i]))
        for i in range(0,len(data)):
            step=agv.process_step_data(data)
        return data,step       
def create_matrix_map(matrix,labelsRFID,labelsLine):
    for i in range(0,len(labelsRFID)):
        x_labels=int((labelsRFID[i].getId().winfo_x()))
        y_labels=int((labelsRFID[i].getId().winfo_y()))
        matrix[int(y_labels/30)][int(x_labels/30)]=1
    
    for i in range(0,len(labelsLine)):
        x_labels=labelsLine[i].getId().winfo_x()
        y_labels=labelsLine[i].getId().winfo_y()  
        heightLine=labelsLine[i].getId().winfo_height()
        widthLine=labelsLine[i].getId().winfo_width()
        if int(widthLine/30)>0:
            for j in range(0,int(widthLine/30)):
                matrix[int(y_labels/30)][int(x_labels/30)+j]=1
        else:
            for j in range(0,int(heightLine/30)):
                matrix[int(y_labels/30)+j][int(x_labels/30)]=1  
    return matrix   
def make_pointstart_and_pointend(matrix,labelsRFID,labelsLine,pathRFID,pathLine,start,end):
    for i in range(0,len(labelsRFID)):
        x_pathRFID=int(labelsRFID[i].getId().winfo_x()/30)
        y_pathRFID=int(labelsRFID[i].getId().winfo_y() /30)
        pathRFID.append((x_pathRFID,y_pathRFID))
        if labelsRFID[i].getStep()==start:
            x_start=int(labelsRFID[i].getId().winfo_x()/30)
            y_start=int(labelsRFID[i].getId().winfo_y() /30)     
        if labelsRFID[i].getStep()==end:
            x=int(labelsRFID[i].getId().winfo_x()/30)
            y=int(labelsRFID[i].getId().winfo_y() /30)   
            matrix[y][x]=10
    for i in range(0,len(labelsLine)):
        x_pathLine=int(labelsLine[i].getId().winfo_x()/30)
        y_pathLine=int(labelsLine[i].getId().winfo_y() /30)
        pathLine.append((x_pathLine,y_pathLine)) 
    return matrix,pathRFID,pathLine,x_start,y_start
def find__item_path(path,pathRFID,pathLine,pathRFID_Item,pathLine_Item):
        for i in range(0,len(path)):
            if path[i] in pathRFID:
                pathRFID_Item.append(path[i])           
        for i in range(0,len(path)):
            if path[i] in pathLine:
                pathLine_Item.append(path[i]) 
        return pathRFID_Item,pathLine_Item  
def make_command(pathRFID_Item,pathLine_Item,command):            
        for i in range(0,len(pathRFID_Item)-1):
            command.append(drive(pathRFID_Item[i],pathRFID_Item[i+1],pathLine_Item[i]))
        return command
def find_RFIDname_in_route(pathRFID_Item,labelsRFID): 
        RFID=[]
        nameRFID=[]
        for i in range(0,len(pathRFID_Item)):
            for j in range(0,len(labelsRFID)):
                x_pathRFID=int(labelsRFID[j].getId().winfo_x()/30)
                y_pathRFID=int(labelsRFID[j].getId().winfo_y() /30)
                if pathRFID_Item[i]==(x_pathRFID,y_pathRFID):
                    nameRFID.append(labelsRFID[j].getName()) 
                    RFID.append(labelsRFID[j])    
        return nameRFID,RFID  
def find_Linename_in_route(pathLine_Item,labelsLine):  
        nameLine=[]
        for i in range(0,len(pathLine_Item)):
            for j in range(0,len(labelsLine)):
                x_pathLine=int(labelsLine[j].getId().winfo_x()/30)
                y_pathLine=int(labelsLine[j].getId().winfo_y() /30)
                if pathLine_Item[i]==(x_pathLine,y_pathLine):
                    nameLine.append(labelsLine[j])   
        return nameLine          
def status_line_in_route(pathLine_Item,labelsLine,ids,head,lenLine,function,line_type,rotate_type,degree_rote,wait_time,speed_max,head_select):    
    for i in range(0,len(pathLine_Item)):
        head.append(head_select)    
        for j in range(0,len(labelsLine)):
            x_pathLine=int(labelsLine[j].getId().winfo_x()/30)
            y_pathLine=int(labelsLine[j].getId().winfo_y() /30)
            if(pathLine_Item[i]==(x_pathLine,y_pathLine)):
                ids.append(labelsLine[j].getId())
                lenLine.append(labelsLine[j].getLength())
                function.append(labelsLine[j].getFunction())
                line_type.append(labelsLine[j].getLinetype())
                rotate_type.append(labelsLine[j].getRotatetype())
                degree_rote.append(labelsLine[j].getDegreerote())  
                wait_time.append(labelsLine[j].getWaittime())
                speed_max.append(labelsLine[j].getSpeedmax())                
    return  ids,head,lenLine,function,line_type,rotate_type,degree_rote,wait_time,speed_max  
def change_type_line(matrix,labelsRFID,labelsLine,command,line_type,head,pathLine_Item,pathRFID_Item):
    status_line=[] 
    _,RFID=find_RFIDname_in_route(pathRFID_Item,labelsRFID)
    nameLine=find_Linename_in_route(pathLine_Item,labelsLine)
    for i in range(0,len(line_type)):
        
        if line_type[i]=="Fork": 
            if command[i]=="Left" and head[i]=="Front":
                line_type[i]="Fork left"
            if command[i]=="Left" and head[i]=="Back":
                line_type[i]="Fork right"
            if command[i]=="Right" and head[i]=="Front":
                line_type[i]="Fork right" 
            if command[i]=="Right" and head[i]=="Back":
                line_type[i]="Fork left"
            
            if command[i]=="Center":
                x_RFID=int(RFID[i].getId().winfo_x()/30)
                y_RFID=int(RFID[i].getId().winfo_y() /30)
                x_Line =int(nameLine[i].getId().winfo_x()/30)
                y_Line= int(nameLine[i].getId().winfo_y()/30)
                if(matrix[y_RFID+1][x_RFID+1]==1)and y_RFID==y_Line and head[i]=="Front":
                    line_type[i]="Fork Right"
                if(matrix[y_RFID+1][x_RFID+1]==1) and y_RFID==y_Line and head[i]=="Back":
                    line_type[i]="Fork Left"    
                if(matrix[y_RFID-1][x_RFID+1]==1) and y_RFID==y_Line and head[i]=="Front":
                    line_type[i]="Fork Left"
                if(matrix[y_RFID-1][x_RFID+1]==1) and y_RFID==y_Line and head[i]=="Back":
                    line_type[i]="Fork Right"  
                    
                if(matrix[y_RFID-1][x_RFID+1]==1) and x_RFID==x_Line and head[i]=="Front":
                    line_type[i]="Fork Right"
                if(matrix[y_RFID-1][x_RFID+1]==1) and x_RFID==x_Line and head[i]=="Back":
                    line_type[i]="Fork Left" 
                if(matrix[y_RFID-1][x_RFID-1]==1) and x_RFID==x_Line and head[i]=="Front":
                    line_type[i]="Fork Left"
                if(matrix[y_RFID-1][x_RFID-1]==1) and x_RFID==x_Line and head[i]=="Back":
                    line_type[i]="Fork Right" 
                
                if(matrix[y_RFID-1][x_RFID-1]==1) and y_RFID==y_Line and head[i]=="Front":
                    line_type[i]="Fork Right"
                if(matrix[y_RFID-1][x_RFID-1]==1) and y_RFID==y_Line and head[i]=="Back":
                    line_type[i]="Fork Left"                     
                if(matrix[y_RFID+1][x_RFID-1]==1) and y_RFID==y_Line and head[i]=="Front":
                    line_type[i]="Fork Left"
                if(matrix[y_RFID+1][x_RFID-1]==1) and y_RFID==y_Line and head[i]=="Back":
                    line_type[i]="Fork Right"    

                    
                if(matrix[y_RFID+1][x_RFID-1]==1) and x_RFID==x_Line and head[i]=="Front":
                    line_type[i]="Fork Right"
                if(matrix[y_RFID+1][x_RFID-1]==1) and x_RFID==x_Line and head[i]=="Back":
                    line_type[i]="Fork Left"                     
                if(matrix[y_RFID+1][x_RFID+1]==1) and x_RFID==x_Line and head[i]=="Front":
                    line_type[i]="Fork Left"
                if(matrix[y_RFID+1][x_RFID+1]==1) and x_RFID==x_Line and head[i]=="Back":
                    line_type[i]="Fork Right"                  
                 

                
    return line_type     
def drag_start(event):
    global pickingHolder
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y 
    pickingHolder = widget        
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)     
def drop_motion(event):
    widget = event.widget
    x = widget.winfo_x()  + event.x
    y = widget.winfo_y()  + event.y
    x = calculateNewCoor(x)             
    y = calculateNewCoor(y)
    widget.place(x=find_nearest(x_info2, x),y=find_nearest(y_info2,y))
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]    
def popup( event):
    aMenu = tk.Menu(root,tearoff=0)
    widget = event.widget
    aMenu.add_command(label='Delete',command=lambda:delete(widget))  
    aMenu.post(event.x_root,event.y_root)   
def delete(widget):

    deleteItem(widget,labelsLine)
    deleteItem(widget,labelsRFID)                

def deleteItem(widget,Item):
    if len(Item)>0:
        try:            
            for i in range(0,len(Item)):
                if(widget==Item[i].getId()):
                    Item.remove(Item[i]) 
                    widget.destroy()                    
        except:                
                pass   

def bfs(grid,start):
    queue = collections.deque([[start]])
    seen = set([start])
    width, height = len(grid[0]), len(grid)
    #print(width,height)
    wall, clear, goal = 0, 1,10
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2)) 
def drive(first_position,last_position,pathLine):
    if first_position[0]==last_position[0] or first_position[1]==last_position[1]:
        return "Center"
    if first_position[0] < last_position[0] and first_position[1]<last_position[1]:
        if first_position[1]==pathLine[1]:
            return "Right"                        
        else:
            return "Left"
            
    if first_position[0] < last_position[0] and first_position[1]>last_position[1]:
        if first_position[1]==pathLine[1] :
            return "Left"                        
        else:
            return "Right"        
    if first_position[0]>last_position[0] and first_position[1]>last_position[1]:
        if first_position[1]==pathLine[1]:
            return "Right"
        else:
            return "Left"
    if first_position[0]>last_position[0] and first_position[1]<last_position[1]:
        if first_position[1]==pathLine[1]:
            return "Left"
        else:
            return "Right"   

        
       
        
if __name__ == '__main__':
    import main
    main.vp_start_gui()





