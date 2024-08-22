N = int(input())
time = list(map(int, input().split()))

time.sort()
s = 0
for i in range(1, N):
    s += time[i-1]
    time[i] += time[i-1]

print(s+time[-1])
