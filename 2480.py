dice = list(map(int, input().split()))
l = len(set(dice))

if(l == 1):
    print(10000 + dice[0] * 1000)
elif(l == 2):
    if(dice[0] != dice[1] and dice[0] != dice[2]):
        print(1000 + dice[1] * 100)
    else:
        print(1000 + dice[0] * 100)
else:
    print(max(dice) * 100)

#이거 살짝 counter 사용해서 할 수도 있을듯