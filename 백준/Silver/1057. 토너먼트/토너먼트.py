import math

N, X, Y = map(int, input().split())

A = min(X, Y)
B = max(X, Y)
ans = 1

while((A%2 == 0) or (B != A+1)):
    A = math.ceil(A/2)
    B = math.ceil(B/2)
    ans += 1

print(ans)