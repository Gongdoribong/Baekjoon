n = int(input())
num = list(map(int, input().split()))
res = []
none = True
for i in range(n):
    for j in range(i-1, -1, -1):
        if num[j] > num[i]:
            print(j+1, end=" ")
            none = False
            break
    if none:
        print(0, end=" ")
