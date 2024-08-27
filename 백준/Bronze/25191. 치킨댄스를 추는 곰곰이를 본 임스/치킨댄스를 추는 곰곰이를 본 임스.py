chicken = int(input())
coke, beer = map(int, input().split())

drink = coke//2+beer
print(min(chicken, drink))
