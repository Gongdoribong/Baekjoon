import sys
hear, look = map(int, input().split())
names = {}
ans = []
for _ in range(hear):
    name = sys.stdin.readline().rstrip('\n')
    names[name] = 1

for _ in range(look):
    name = sys.stdin.readline().rstrip('\n')
    look = names.get(name, 0)
    if look:
        ans.append(name)



print(len(ans))
ans.sort()
for i in ans:
    print(i)
