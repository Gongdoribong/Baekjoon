n = int(input())
t = list(map(int, input().split()))
t.sort()

if n%2 == 0:
    m = 0
else:
    m = t.pop()

t1 = t[:n//2]
t2 = t[n//2:]

for i in range(n//2):
    m = max(m, t1[i]+t2[-i-1])

print(m)

