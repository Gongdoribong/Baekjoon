import sys

class Stack() :
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop()

    def isEmpty(self):
        if self.stack:
            return 0
        else:
            return 1
        
    def sum(self):
        return sum(self.stack)


s = Stack()
k = int(sys.stdin.readline())
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        s.pop()
    else: 
        s.push(n)

print(s.sum())