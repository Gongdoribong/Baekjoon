import math
N, M = map(int, input().split())
search = list(map(int, input().split()))
nums = [x for x in range(1, N+1)]
loc = 0
act = 0
for i in search:
    dist = abs(loc - nums.index(i))
    if dist > math.floor(len(nums)/2):
        act += len(nums)%dist
    else:
        act += dist
    loc = nums.index(i)
    nums.pop(loc)
print(act)