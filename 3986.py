def solution():
    word = list(input())
    A = [0,0]
    B = [0,0]

    for i in word:
        if i == 'A':
            if A[0] == 0:
                A[0] += 1
            elif B[0] == 0:
                A[0] -= 1
            else:
                return 0
        elif i == 'B':
            if B[0] == 0 :
                B[0] += 1
            elif A[0] == 0:
                B[0] -= 1
            else:
                return 0
    if A[0] != 0 or A[1] != 0 or B[0] != 0 or B[1] != 0:
        return 0
    return 1

n = int(input())
cnt = 0

for _ in range(n):
    if(solution() == 1):
        cnt += 1

print(cnt)
