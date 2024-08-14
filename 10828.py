import sys

class Stack() :
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def empty(self):
        if self.stack:
            return 0
        else:
            return 1
        
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]
        
s = Stack()
n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().split()
    cmd = word[0]
    if cmd == 'push':
        s.push(int(word[1]))
    elif cmd == 'pop':
        print(s.pop())
    elif cmd == 'size':
        print(s.size())
    elif cmd == 'empty':
        print(s.empty())
    elif cmd == 'top':
        print(s.top())
