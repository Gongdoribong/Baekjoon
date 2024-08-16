while(True):
    num = list(map(int, input().split()))
    if(num[0]==num[1]==num[2]==0):
        break
    diag = num.pop(num.index(max(num)))
    if(diag**2 == num[0]**2 + num[1]**2):
        print("right")
    else:
        print("wrong")
    
