import sys
N, M = map(int, input().split())
like = []
for n in range(N):
    like.append(list(map(int, sys.stdin.readline().split())))

res = 0


for i in range(M):
    for j in range(i, M):
        for k in range(j, M):
            sum = 0
            for l in range(N):
                sum += max(like[l][i], like[l][j], like[l][k])
            if res < sum:
                res = sum

print(res)

