import sys

def fact(n):
    if n==1:
        return 1
    return n + fact(n-1)

while(True):
    a = int(sys.stdin.readline())
    if(a == 0):
        break
    print(fact(a))
