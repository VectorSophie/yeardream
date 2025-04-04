
import heapq
class PriorityQueue:

    def __init__(self) :
        self.data = []

    def push(self, value) :
        
        heapq.heappush(self.data, value)

    def top(self) :
        
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]


    def pop(self) :
        
        if len(self.data) > 0:
            heapq.heappop(self.data)

def heapSort(items) :
   
    result = []

    pq = PriorityQueue()

    for item in items:
        pq.push(item)
    
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result