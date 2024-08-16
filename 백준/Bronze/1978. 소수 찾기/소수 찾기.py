N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in nums:
    flag = 1
    if i == 1:
        continue
    for j in range(2, int(i**(1/2))+1):
        if i%j == 0:
            flag = 0
            break
    if flag:
        cnt+=1

print(cnt)
