T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    dist = (N//H)+1
    if(floor == 0):
        floor = H
        dist -= 1


    if dist<10:
        print(str(floor)+"0"+str(dist))
    else:
        print(str(floor)+str(dist))
