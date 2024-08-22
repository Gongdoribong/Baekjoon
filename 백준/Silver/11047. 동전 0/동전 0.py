N, K = map(int, input().split())
kind = [0]*N
for i in range(N-1, -1, -1):
    kind[i] = int(input())

last = K
sum = 0
for i in range(N):
    if last == 0:
        break
    if kind[i] > last:
        continue
    else:
        sum += last//kind[i]
        last -= (last//kind[i])*kind[i]

print(sum)
