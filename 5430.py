import sys
T = int(sys.stdin.readline())

for _ in range(T):
    cmd = sys.stdin.readline()
    n = int(sys.stdin.readline())
    sarr = sys.stdin.readline()
    sarr = sarr[1:-2]
    if sarr:
        sarr = list(map(int, sarr.split(',')))
    else:
        sarr = []
    cur = 0
    error = False
    
    for i in cmd:
        if i == 'R' and sarr:
            sarr.reverse()
        elif i == 'D':
            if cur >= n-1:
                error = True
                print('error')
                break
            else:
                cur += 1
    if error == False:
        print(sarr)
