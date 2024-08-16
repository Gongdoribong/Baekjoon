N, blackJack = map(int, input().split())
cards = list(map(int, input().split()))

flag = False
can = 0

cards.sort(reverse=True)

for i in range(N):
    for j in range(i):
        for k in range(j):
            cardSum = cards[i]+cards[j]+cards[k]
            if cardSum== blackJack:
                flag = True
                print(cardSum)
                break
            elif cardSum < blackJack:
                can = max(cardSum, can)
                break
        if flag:
            break
    if flag:
        break

if not flag:
    print(can)
