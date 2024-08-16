N, M, K = map(int, input().split())
res = (M+(K-3))%N
if(res == 0):
    res = N
print(res)
