N, M = map(int, input().split())
mp = []
emptyRow = 0
emptyCol = 0
for _ in range(N):
    line = list(input())
    mp.append(line)
    if 'X' not in line:
        emptyRow += 1

changeMap = list(map(list, zip(*mp)))

for i in range(M):
    if 'X' not in changeMap[i]:
        emptyCol += 1

print(max(emptyRow, emptyCol))
