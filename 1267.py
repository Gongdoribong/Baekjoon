def youngSik(fees) :
    sum = 0
    for i in fees :
        sum += (i // 30 + 1) * 10
    return sum

def minSik(fees) :
    sum = 0
    for i in fees :
        sum += (i // 60 + 1) * 15
    return sum

N = int(input())
fees = list(map(int, input().split()))

y = youngSik(fees)
m = minSik(fees)

if y < m :
    print('Y', y)
elif m < y :
    print('M', m)
else :
    print('Y', 'M', y)