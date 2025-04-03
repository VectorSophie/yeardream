from queue import Queue

def BFS(tree) :
    q = Queue()
    q.put(tree)
    result = []
    while len(q.queue)>0:
        cur = q.get()
        if cur == None:
            continue
        result.append(cur.index)
        q.put(cur.left)
        q.put(cur.right)

    return result