import sys
class Queue:
    def __init__(self):
        self.head = -1
        self.tail = -1
        self.que = list()

    def push(self, item):
        self.tail += 1
        self.que.append(item)

    def pop(self):
        if not self.empty():
            self.head += 1
            tmp = self.que[self.head]
            return tmp
        else:
            return -1
        
    def size(self):
        return(self.tail - self.head)
    
    def empty(self):
        if self.head == self.tail:
            return 1
        else:
            return 0
        
    def front(self):
        if not self.empty():
            return(self.que[self.head+1])
        else:
            return -1
    
    def back(self):
        if not self.empty():
            return(self.que[self.tail])
        else:
            return -1
        

q = Queue()
N = int(sys.stdin.readline())
for i in range(N):
    q.push(i+1)

while q.size() != 1:
    q.pop()
    q.push(q.pop())

print(q.pop())