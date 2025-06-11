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
       
        if len(self.myQueue) == 0:
            return 1
        else:
            return 0

    def front(self) :
        
        if len(self.myQueue) == 0:
            return -1
        else:
            return self.myQueue[0]

    def back(self) :
        
        if len(self.myQueue) == 0:
            return -1
        else:
            return self.myQueue[len(self.myQueue)-1]
        
class orderInfo:
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders):
    normalInd = normalQueue.front()
    vipInd = vipQueue.front()

    if vipInd == -1:
        return normalQueue
    if normalInd == -1:
        return vipQueue

    if time < orders[normalInd].time and time < orders[vipInd].time:
        return vipQueue

        if orders[vipInd].time <= orders[normalInd].time:
            return vipQueue
        else:
            return normalQueue

    if time >= orders[normalInd].time and time < orders[vipInd].time:
        return normalQueue

    if time >= orders[vipInd].time and time < orders[normalInd].time:
        return vipQueue

    return vipQueue

def processOrder(orders):
    result = []
    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.push(i)
        else:
            vipQueue.push(i)

        while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1):
            target = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            index = target.front()

            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

            result.append(index + 1)
            target.pop()

    while not (normalQueue.empty() == 1 and vipQueue.empty() == 1):
        target = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
        index = target.front()

        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

        result.append(index + 1)
        target.pop()

    return result