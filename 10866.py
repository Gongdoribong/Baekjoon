import sys
class Deque:
    def __init__(self, length):
        self.length = length
        self.head = 0
        self.tail = 0
        self.deq = [0]*length

    def push_front(self, item):
        self.head = ( self.head -  1 + self.length ) % self.length
        self.deq[self.head] = item

    def push_back(self, item):
        self.deq[self.tail] = item
        self.tail = ( self.tail + 1) % self.length

    def pop_front(self):
        if not self.empty():
            tmp = self.deq[self.head]
            self.head = ( self.head + 1) % self.length
            return tmp
        else:
            return -1
        
    def pop_back(self):
        if not self.empty():
            self.tail = ( self.tail -  1 + self.length ) % self.length
            tmp = self.deq[self.tail]
            return tmp
        else:
            return -1
        
    def size(self):
        return((self.length - self.head) % self.length + self.tail)
    
    def empty(self):
        if self.head == self.tail:
            return 1
        else:
            return 0
        
    def front(self):
        if not self.empty():
            return(self.deq[self.head])
        else:
            return -1
    
    def back(self):
        if not self.empty():
            return(self.deq[(self.tail-1 + self.length) % self.length])
        else:
            return -1
        

N = int(sys.stdin.readline())
q = Deque(N)
for _ in range(N):
    s = sys.stdin.readline().split()
    cmd = s[0]

    if cmd == 'push_front':
        q.push_front(int(s[1]))

    elif cmd == 'push_back':
        q.push_back(int(s[1]))

    elif cmd == 'pop_front':
        print(q.pop_front())

    elif cmd == 'pop_back':
        print(q.pop_back())

    elif cmd == 'size':
        print(q.size())

    elif cmd == 'empty':
        print(q.empty())

    elif cmd == 'front':
        print(q.front())

    elif cmd == 'back':
        print(q.back())
