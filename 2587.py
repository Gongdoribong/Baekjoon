numList = []
for i in range(5):
    numList.append(int(input()))

numList = sorted(numList)

print(sum(numList)//len(numList))
print(numList[len(numList)//2])
