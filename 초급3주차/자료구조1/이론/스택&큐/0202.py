class Queue:
    
    def __init__(self) :
        
        self.myQueue = []

    def push(self, n) :
        
        self.myQueue.append(n)

    def pop(self) :
        
        if self.empty() == 1:
            return

        del self.myQueue[0]


    def size(self) :
        
        return len(self.myQueue)

    def empty(self) :
        
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self) :
        
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[0]

    def back(self) :
    
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[-1]
        
        