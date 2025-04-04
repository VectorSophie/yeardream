import heapq
def find_mid(nums) :
    n = len(nums)
    result = []

    l = []
    r = []

    for i in range(n):
        x = nums[i]

        if not l or not r:
            heapq.heappush(l, -x)
        else:
            if x >= -l[0]:
                heapq.heappush(r,x)
            else:
                heapq.heappush(l,-x)
        while not (len(l) == len(r) or len(l) == len(r)+1):
            if len(l) > len(r):
                heapq.heappush(r,-heapq.heappop(l))
            else:
                heapq.heappush(l,-heapq.heappop(r))
        result.append(-l[0])

    
    return result