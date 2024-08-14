from itertools import combinations

dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
tSum = sum(dwarf)
goal = tSum - 100
ect = []

for i in combinations(dwarf, 2):
    if sum(i) == goal :
        ect.append(dwarf.index(i[0]))
        ect.append(dwarf.index(i[1]))
        break

for j in range(9) :
    if j not in ect:
        print(dwarf[j])
