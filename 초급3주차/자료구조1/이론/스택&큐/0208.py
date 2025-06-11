from queue import Queue

def josephus_sequence(n, k) :

    q = Queue()

    result = []

    for i in range(1, n+1):
        q.put(i)

    while not q.empty():
        for i in range(k):
            num = q.get()

            if i == k - 1:
                result.append(num)
            else:
                q.put(num)
            
    return result