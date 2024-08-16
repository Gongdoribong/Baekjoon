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

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        if self.stack:
            return 0
        else:
            return 1
        
    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]
        

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
s = Stack()

res = [0]*n

for j in range(len(towers)):
    b = False
    i = towers[j]

    while(not s.isEmpty()): #스택이 안비어있을 때
        if(s.top()[1]<i):   #탑이 작으면 pop
            s.pop()
        else:   #탑이 크면 기록
            res[j] = s.top()[0]+1
            break

    s.push([j,i])   #push
    

print(*res)
