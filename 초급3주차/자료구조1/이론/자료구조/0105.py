class orderManager :
    
    def __init__(self) :
        
        self.data = []

    def addOrder(self, orderId) :
        
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        
        for i in range(len(self.data)):
            if self.data[i] == orderId:
                return(i+1)
        return -1