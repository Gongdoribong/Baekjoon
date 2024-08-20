space, basket = map(int, input().split())
appleNum = int(input())
basketL = 0
basketR = basket - 1
dist = 0
for _ in range(appleNum):
    appleLoc = int(input()) - 1
    if appleLoc > basketR:  #사과가 바구니 오른쪽에 있다면
        dist += appleLoc - basketR
        basketR = appleLoc
        basketL = basketR - basket + 1
    elif appleLoc < basketL:    #사과가 바구니 왼쪽에 있다면
        dist += basketL - appleLoc
        basketL = appleLoc
        basketR = basketL + basket -1
    else:   #사과가 바구니 안에 있다면
        continue

print(dist)

