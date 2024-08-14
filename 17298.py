import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    none = True
    for j in range(i+1, n):
        if A[i] < A[j]:
            print(A[j], end=" ")
            none = False
            break
    if none:
        print(-1, end=" ")