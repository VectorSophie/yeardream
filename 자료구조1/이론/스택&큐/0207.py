class Stack:
    
    def __init__(self) :
        
        self.myStack = []

    def push(self, n) :
        
        self.myStack.append(n)

    def pop(self) :
        
        if self.size() == 0:
            return
        else:
            self.myStack.pop()

    def size(self) :
        
        return len(self.myStack)

    def empty(self) :
        
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self) :

        if self.empty() == 1:
            return -1
        else:
            return self.myStack[-1]

def notepad(s, commands) :
    left = list(s)
    right = []

    for line in commands:
        command = line.split()
        action = command[0]

        if action == "L":
            if len(left) > 0:
                v = left.pop()
                right.append(v)
        elif action == "R":
            if len(right) > 0:
                v = right.pop()
                left.append(v)
        elif action == "D":
            if len(left) > 0:
                left.pop()
        elif action == "P":
            left.append(command[1])

    result = left + right[::-1]

    return "".join(result)