import sys

N = int(input())
if N > 10000:
    l = [0]*10000
    for i in range(N):
        l[int(sys.stdin.readline())-1] += 1
    for i in range(10000):
        for j in range(l[i]):
            print(i+1)
else:
    l=[]
    for i in range(N):
        l.append(int(sys.stdin.readline()))

    l.sort()

    for i in range(len(l)):
        print(l[i])
