N = int(input())
words = []
res = 0

for i in range(N):
    cnt = 0 
    letter = set()
    words.append(input())
    for j in words[i]:
        if(j not in letter):
            letter.add(j)
            last = j
        else:
            if(j != last):
                cnt += 1
    if(cnt == 0):
        res += 1

print(res)
