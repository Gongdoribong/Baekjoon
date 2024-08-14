A, B, N = input().split()
A = int(A)
B = int(B)
N = int(N)

divide = round(A/B,N+1)
result = list(str(divide))

print(int(result[len(result)-2]))
