import sys
    
T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    cache = [0 for _ in range(N+2)]
    cache[1] = 1
    
    for i in range(2, N+1):
        cache[i] = cache[i-1] + cache[i-2]
    if N == 0:
        cnt0 = 1
        cnt1 = 0
    elif N == 1:
        cnt0 = 0
        cnt1 = 1
    elif N == 2:
        cnt0 = 1
        cnt1 = 1
    else:
        cnt0 = cache[N-2] + cache[N-3]
        cnt1 = cache[N-2]*2 + cache[N-3]

    print(cnt0, cnt1)
