class LinkedListElement :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext
        
class orderManager :
    def __init__(self) :
        self.start = None
        self.end = None

    def addOrder(self, orderId) :
        o = LinkedListElement(orderId, None, None)

        if self.start == None and self.end == None:
            self.start = o
            self.end = o
        else:
            self.end.myNext = o
            o.myPrev = self.end

            self.end = o

    def removeOrder(self, orderId) :

        if self.start == None and self.end == None:
            return

        current = self.start

        while current != None:
            if current.data == orderId:
                prevElem = current.myPrev
                nextElem = current.myNext

                if prevElem != None:
                    prevElem.myNext = nextElem

                if nextElem != None:
                    nextElem.myPrev = prevElem

                if current == self.end:
                    self.end = prevElem

                if current == self.start:
                    self.start = nextElem

            current = current.myNext

    def getOrder(self, orderId) :
        cnt = 0

        if self.start == None and self.end == None:
            return -1

        current = self.start

        while current != None:
            if current.data == orderId:
                return cnt + 1
            
            current = current.myNext
            cnt = cnt + 1    

        return -1
