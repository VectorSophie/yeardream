class Queue:
    def __init__(self):
        self.myQueue = []

    def push(self, n):
        self.myQueue.append(n)

    def pop(self):
        if self.empty() == 1:
            return
        del self.myQueue[0]

    def size(self):
        return len(self.myQueue)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return -1 if self.empty() == 1 else self.myQueue[0]

    def back(self):
        return -1 if self.empty() == 1 else self.myQueue[-1]

class orderInfo:
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normQueue, vipQueue, time, orders):
    normInd = normQueue.front()
    vipInd = vipQueue.front()

    if vipInd == -1:
        return normQueue
    if normInd == -1:
        return vipQueue

    if time < orders[normInd].time and time < orders[vipInd].time:
        return vipQueue

    if orders[vipInd].time <= orders[normInd].time:
        return vipQueue
    else:
        return normQueue

    if time >= orders[normInd].time and time < orders[vipInd].time:
        return normQueue

    if time >= orders[vipInd].time and time < orders[normInd].time:
        return vipQueue

    return vipQueue

def processOrder(orders):
    result = []
    normQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normQueue.push(i)
        else:
            vipQueue.push(i)

        while jobEndTime <= curTime and not (normQueue.empty() == 1 and vipQueue.empty() == 1):
            target = selectQueue(normQueue, vipQueue, jobEndTime, orders)
            index = target.front()

            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

            result.append(index + 1)
            target.pop()

    while not (normQueue.empty() == 1 and vipQueue.empty() == 1):
        target = selectQueue(normQueue, vipQueue, jobEndTime, orders)
        index = target.front()

        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

        result.append(index + 1)
        target.pop()

    return result
