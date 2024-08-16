import math

n, k = map(int, input().split())

stu = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
cnt = 0

for i in range(n):
    s, g = map(int, input().split())
    stu[s][g-1] += 1

for i in range(2):
    for j in stu[i]:
        cnt += math.ceil(j/k)

print(cnt)
