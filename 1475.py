import math
a = list(map(int, input()))

esc = False
num = max(a, key=a.count)
cnt = a.count(num)

if num==6 or num==9:
    for i in range(10):
        if i!=num and a.count(i) == cnt:
            num == i
            esc = True
            print(cnt)
            break
    if esc == False:
        n6 = a.count(6)
        n9 = a.count(9)
        max = max(n6, n9)
        min = min(n6, n9)
        res = min + math.ceil((max - min)/2)
        print(res)
else:
    print(cnt)
