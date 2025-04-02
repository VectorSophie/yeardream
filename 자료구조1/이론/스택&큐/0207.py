from queue import Queue

class orderInfo:
    
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue,vipQueue, time, orders):
    normalInd = -1 if len(normalQueue.queue) == 0 else normalQueue.queue[0]
    vipInd = -1 if len(vipQueue.queue) == 0 else vipQueue.queue[0]

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

def processOrder(orders) :
    result = []

    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

   
    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.put(i)
        else:
            vipQueue.put(i)

        while jobEndTime <= curTime and not(normalQueue.empty() and vipQueue.empty()):
            target = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            index = target.queue[0]

            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

            result.append(index + 1)
            target.get()

    while not (normalQueue.empty()and vipQueue.empty()):
        target = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
        index = target.queue[0]

        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration

        result.append(index + 1)
        target.get()
    return result