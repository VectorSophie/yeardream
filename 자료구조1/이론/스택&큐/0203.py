'''
CheckParen 함수를 완성하세요.
단, Stack 클래스를 사용하세요.
'''

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


def checkParen(p) :

    s = Stack()

    for c in p:
        if c == '(':
            s.push(c)
        else:
            if s.empty() == 1:
                return "NO"
            s.pop()
    if s.empty() == 1:
        return "YES"
    else:
        return "NO"