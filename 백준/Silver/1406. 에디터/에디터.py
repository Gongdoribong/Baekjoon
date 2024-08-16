import sys

#스택 구현
class Stack() :
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        if self.stack:
            return 0
        else:
            return 1
        
    def rev(self):
        self.stack.reverse()

    def p(self):
        print(self.stack)
        

left = Stack()
right = Stack()

s = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

#초기 문자 집어넣기
for i in s:
    left.push(i)

#커서 이동
for i in range(n):
    line = sys.stdin.readline().strip().split(' ')
    cmd = line[0]
    if(cmd == 'P'):
        left.push(line[1])
    elif(cmd == 'L'):
        if(not left.isEmpty()):
            right.push(left.pop())
    elif(cmd == 'D'):
        if(not right.isEmpty()):
            left.push(right.pop())
    else:
        if(not left.isEmpty()):
            left.pop()

#결과 출력
left.rev()
for _ in range(left.size()):
    print(left.pop(), end='')

for _ in range(right.size()):
    print(right.pop(), end='')