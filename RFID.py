class RFID:
    def __init__(self,step,ids,name):
        self.step=step
        self.ids=ids
        self.name = name        
    def getStep(self):
        return self.step
    def getId(self):
        return self.ids        
    def getName(self):
        return self.name

    
