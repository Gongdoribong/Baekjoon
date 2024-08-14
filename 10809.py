s = list(input())
cnt = [-1]*26

for i in s:
    cnt[ord(i)-97] = s.index(i)

print(*cnt)
