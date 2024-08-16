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
        
    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

s = Stack()
n = int(input())
num = []
s_num = []
res = []
cursor = 0
i = 0

for _ in range(n):
    num.append(int(input()))

s_num = sorted(num)

while(cursor < n):
    if(s.top() == num[cursor]):
        s.pop()
        res.append('-')
        cursor += 1
    elif(i < len(s_num)):
        s.push(s_num[i])
        res.append('+')
        i += 1
    else:
        break
s.pop()
if s.isEmpty():
    for i in range(len(res)):
        print(res[i])
else:
    print("NO")
