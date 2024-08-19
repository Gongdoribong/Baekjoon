T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r1+r2 > dist and abs(r1-r2) < dist:
        print(2)
    elif r1+r2 == dist or abs(r1-r2) == dist:
        print(1)
    elif r1+r2 < dist or abs(r1-r2) > dist:
        print(0)
