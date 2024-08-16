import math
t, x, m = map(int, input().split())
safeTime = [1000001]

for _ in range(m):
    md, ms = map(int, input().split())
    safeTime.append(math.floor((md-1)/ms))

s = min(safeTime)

if t<s:
    gain = t*x
elif s == 0:
    gain = 0
else:
    gain = (s + math.floor((t-s)/2))*x

print(gain)
