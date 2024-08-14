import sys
sys.setrecursionlimit(100000)

def first_route(i, j):
    return route(i, j-1)+route(i-1,j-1)


def route(i, j):
    if(i==1 or j==1):
        return 1
    return route(i-1, j)+route(i, j-1)+route(i-1,j-1)

n, m = map(int, input().split(" "))
s = (first_route(n, m)*2)+1

print(s)