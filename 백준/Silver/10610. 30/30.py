N = input()
intN = sorted([int(i) for i in N], reverse=True)
if '0' not in N or sum(intN)%3 != 0:
    print(-1)
else:
    print(int(''.join(sorted(N, reverse=True))))
