N = int(input())
first = list(input())
l = len(first)
for i in range(N-1):
    cmp = list(input())
    for j in range(l):
        if first[j] != cmp[j]:
            first[j] = '?'

print("".join(first))
