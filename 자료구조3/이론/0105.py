import heapq

def getMinForce(weights) :
    pq = []
    for w in weights:
        heapq.heappush(pq,w)
    result = 0
    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)

        temp = x + y
        result = result + temp

        heapq.heappush(pq,temp)


    return result