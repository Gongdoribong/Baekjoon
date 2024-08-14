def solution(s):
    bracket = list(s)
    cnt = [0,0]

    for i in bracket:
        if(i=="("):
            cnt[0] += 1
        else:
            cnt[1] += 1
        
        if(cnt[0] < cnt[1]):
            return "NO"

        elif(cnt[0]==cnt[1]):
            cnt[0] = 0
            cnt[1] = 0

    if(cnt[0]!=cnt[1]):
        return "NO"

    return "YES"

n = int(input())
for _ in range(n):
    print(solution(list(input())))