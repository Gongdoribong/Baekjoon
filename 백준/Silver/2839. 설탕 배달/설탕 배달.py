N = int(input())
beep = [1, 2, 4, 7]
cnt = 0
while(True):
    if N == 0:
        print(cnt)
        break
    if N in beep:
        print(-1)
        break

    if N%5 == 0:
        cnt += N//5
        N = 0

    elif (N%5)%3 == 0:
        cnt += N//5
        N = N%5
        cnt += N//3
        N = 0
    
    elif (N-5) not in beep:
        cnt += 1
        N -= 5
    
    elif (N-3) not in beep:
        cnt += 1
        N -= 3

    else:
        print(-1)
        break
