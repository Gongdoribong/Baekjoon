n = int(input())

for i in range(n):
    r, s = input().split()
    r = int(r)
    for j in s:
        print(j*r, end="")
    print()
