woods = list(map(int, input().split()))
ans = [1, 2, 3, 4, 5]

while(True):
    for i in range(1,5):
        if woods[i-1] > woods[i]:
            tmp = woods[i-1]
            woods[i-1] = woods[i]
            woods[i] = tmp
            print(*woods)
    if woods == ans:
        break
