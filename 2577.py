a = 1
for _ in range(3) :
    a *= int(input())
cnt = [0]*10
nums = list(map(int, str(a)))

for i in nums:
    cnt[i] += 1

for i in cnt :
    print(i)

