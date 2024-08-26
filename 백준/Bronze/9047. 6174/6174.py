import sys

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    while(True):
        if n == 6174:
            print(cnt)
            break
        l = f"{n:04d}"
        m = int(''.join(sorted(l)))
        M = int(''.join(sorted(l, reverse=True)))
        n = M-m
        cnt += 1
