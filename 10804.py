nums = [x+1 for x in range(20)]
for _ in range(10) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range((b-a+1)//2) :
        tmp = nums[a+i]
        nums[a+i] = nums[b-i]
        nums[b-i] = tmp

print(*nums)
