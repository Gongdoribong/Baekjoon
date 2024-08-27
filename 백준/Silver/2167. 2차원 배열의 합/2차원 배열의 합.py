import sys

N, M = map(int, sys.stdin.readline().split())
m = []
for _ in range(N):
    m.extend((map(int, sys.stdin.readline().split())))

K = int(input())
for _ in range(K):
    res = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    # for k in range(i-1, x):
    #     for l in range(j-1, y):
    #         sum += m[k][l]
    i -=1
    j -=1
    x -=1
    y -=1
    for k in range(i, x+1):
        res += sum(m[(k*M)+j:(k*M)+y+1])

    print(res)
