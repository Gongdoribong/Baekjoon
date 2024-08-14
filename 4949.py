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
        
def check():
    s = Stack()
    words = list(input())
    if(len(words) == 1 and words[0] == '.'):
        return -1
    for i in range(len(words)):
        ch = words[i]
        if ch == '(' or ch == '[':
            s.push(ch)
        elif ch == ')' or ch == ']':
            if(s.isEmpty()) : return 0
            else:
                open_ch = s.pop()
                if((open_ch == '(' and ch != ')') or (open_ch == '[' and ch != ']')):
                    return 0
    if(s.isEmpty() == 0): return 0
    return 1
n = 0
while(n != -1):
    n = check()
    if n == -1:
        break
    elif n == 1:
        print('yes')
    elif n == 0:
        print('no')