T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    dist = (N//H)+1
    if(floor == 0):
        floor = H
        dist -= 1

    print(str(floor)+format(str(dist)).zfill(2))
