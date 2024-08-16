A = list(map(int, input().split()))
A.sort()
res = []

if A[0] == A[1] :
    n = 0

else:
    n = A[1] - A[0] -1
    for i in range(A[0]+1, A[1]) :
        res.append(i)

    res.sort()

print(n)
print(*res)
