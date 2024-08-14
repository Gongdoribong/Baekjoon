while True:
    a, b, c = map(int, input().split())
    if(a==b==c==0):
        break
    if((a+c)/2 == b):
        nextNum = c+(b-a)
        print(f"AP {nextNum}")
    elif((a*c)**(1/2) == b):
        nextNum = c*(b//a)
        print(f"GP {nextNum}")
