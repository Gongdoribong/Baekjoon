import math
up, dn, tree = map(int, input().split())

goal = tree-up
go = up-dn

day = math.floor(goal/go)
if(goal%go == 0):
    day += 1
else:
    day += 2

print(day)
