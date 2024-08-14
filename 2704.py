T = int(input())

for _ in range(T):
    clock=[]
    H, M, S = map(int, input().split(":"))
    clock.append(list(format(H, 'b').zfill(6)))
    clock.append(list(format(M, 'b').zfill(6)))
    clock.append(list(format(S, 'b').zfill(6)))
    clockT = list(map(list, zip(*clock)))
    res1 = ''.join(sum(clockT, []))
    res2 = ''.join(sum(clock, []))
    print(res1, res2)
