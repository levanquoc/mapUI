class Line:
    def __init__(self,step,ids,length,function,head,rotate_type,degree_rote,command,line_type,speed_max,wait_time):
        self.step=step
        self.ids = ids
        self.length=length
        self.function=function
        self.head=head
        self.rotate_type=rotate_type
        self.degree_rote=degree_rote
        self.command=command
        self.line_type=line_type
        self.speed_max=speed_max
        self.wait_time=wait_time

    def getStep(self):
    
        return self.step
        
    def getId(self):
    
        return self.ids

    def getLength(self):
    
        return self.length       

    def getFunction(self):
    
        return self.function
        
    def getHead(self):
    
        return self.head    
    
    def getRotatetype(self):
    
        return self.rotate_type
    def getDegreerote(self):
    
        return self.degree_rote
        
    def getCommand(self):
    
        return self.command
    
    def getLinetype(self):
    
        return self.line_type
        
    def getSpeedmax(self):
    
        return self.speed_max

    def getWaittime(self):
    
        return self.wait_time 
    def setStep(self,step):
    
        self.step=step
        
    def setId(self,ids):
    
        self.ids=ids

    def setLength(self,length):
    
        self.length =length      

    def setFunction(self,function):
    
        self.function=function
        
    def setHead(self,head):
    
        self.head =head   
    
    def setRotatetype(self,rotate_type):
        self.rotate_type=rotate_type
        
    def setDegreerote(self,degree_rote):
    
        self.degree_rote=degree_rote
        
    def setCommand(self,command):
    
        self.command=command
    
    def setLinetype(self,line_type):
    
        self.line_type=line_type
        
    def setSpeedmax(self,speed_max):
    
        self.speed_max=speed_max

    def setWaittime(self,wait_time):
    
        self.wait_time=wait_time         

