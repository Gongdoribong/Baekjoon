N = input()
intN = [int(i) for i in N]
if '0' not in N or sum(intN)%3 != 0:
    print(-1)
else:
    print(int(''.join(sorted(N, reverse=True))))
