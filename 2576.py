oddList = []

for i in range(7):
    n = int(input())
    if(n%2 != 0):
        oddList.append(n)

if(len(oddList)==0):
    print(-1)
else:
    print(sum(oddList))
    print(min(oddList))
