import sys
T = int(input())
for _ in range(T):
    n = int(input())
    cloth = {}
    res = 1

    for _ in range(n):
        name, kind = map(str, sys.stdin.readline().split())
        if kind in cloth:
            cloth[kind] += 1
        else:
            cloth[kind] = 2
    for i in cloth.values():
        res *= i

    print(res-1)
