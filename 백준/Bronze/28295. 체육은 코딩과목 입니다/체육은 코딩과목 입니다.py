s = 0
for _ in range(10):
    c = int(input())
    if c == 1:
        s += 90
    elif c == 2:
        s += 180
    elif c == 3:
        s -= 90

if s < 0:
    t = abs(s//90)%4
    if  t == 1:
        print("W")
    elif t == 2:
        print("S")
    elif t == 3:
        print("E")
    elif t == 0:
        print("N")
elif s > 0:
    t = (s//90)%4
    if  t == 1:
        print("E")
    elif t == 2:
        print("S")
    elif t == 3:
        print("W")
    elif t == 0:
        print("N")
elif s == 0:
    print("N")
