class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

class LinkedListPipe:
    
    def __init__(self) :
        
        self.myPipe = []
        self.start = None
        self.end = None
        pass

    def addLeft(self, n) :
        
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)

            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, self.start)

            self.start = elem


    def addRight(self, n) :
        
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)

            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, None)

            self.end.myNext = elem

            self.end = elem

    def getBeads(self) :

        result = []
        current = self.start

        while current != None:
            result.append(current.value)
            current = current.myNext
        return result
def processBeads(myInput) :

    myPipe = LinkedListPipe()

    for x,y in myInput:
        if y == 0:
            myPipe.addLeft(x)
        elif y == 1:
            myPipe.addRight(x)
    return myPipe.getBeads()

    result = []

    return result