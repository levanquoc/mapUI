class Line:
    def __init__(self,ids,length,function,line_type,rotate_type,degree_rote,speed_max,wait_time):
        
        self.ids = ids
        self.length=length
        self.function=function 
        self.line_type=line_type
        self.rotate_type=rotate_type
        self.degree_rote=degree_rote         
        self.speed_max=speed_max
        self.wait_time=wait_time


        
    def getId(self):
    
        return self.ids

    def getLength(self):
    
        return self.length       

    def getFunction(self):
    
        return self.function 
        
    def getLinetype(self):
    
        return self.line_type
        
    def getRotatetype(self):
    
        return self.rotate_type
    def getDegreerote(self):
    
        return self.degree_rote            
        
    def getSpeedmax(self):
    
        return self.speed_max

    def getWaittime(self):
    
        return self.wait_time 

        
    def setId(self,ids):
    
        self.ids=ids

    def setLength(self,length):
    
        self.length =length      

    def setFunction(self,function):
    
        self.function=function   
        
    def setLinetype(self,line_type):
    
        self.line_type=line_type
        
    def setRotatetype(self,rotate_type):
    
        self.rotate_type=rotate_type
        
    def setDegreerote(self,degree_rote):
    
        self.degree_rote=degree_rote
    
        
    def setSpeedmax(self,speed_max):
    
        self.speed_max=speed_max

    def setWaittime(self,wait_time):
    
        self.wait_time=wait_time         

