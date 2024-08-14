n = list(map(int, input().split(" ")))
burger = list(map(int, input().split(" ")))
side = list(map(int, input().split(" ")))
drink = list(map(int, input().split(" ")))

discNum = min(n)
oriSum = sum(burger)+sum(side)+sum(drink)

discBg = []
discSide = []
discDrink = []

for i in range(discNum):
    bgMaxIdx = burger.index(max(burger))
    discBg.append(burger.pop(bgMaxIdx)*0.9)
    sideMaxIdx = side.index(max(side))
    discSide.append(side.pop(sideMaxIdx)*0.9)
    drinkMaxIdx = drink.index(max(drink))
    discDrink.append(drink.pop(drinkMaxIdx)*0.9)

discSum = sum(burger)+sum(side)+sum(drink)+sum(discBg)+sum(discSide)+sum(discDrink)

print(oriSum)
print(int(discSum))
