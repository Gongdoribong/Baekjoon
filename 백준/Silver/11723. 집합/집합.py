import sys

M = int(input())
s = [0]*20
for _ in range(M):
    line = list(sys.stdin.readline().split())
    com = line[0]

    if com == 'add':
        x = int(line[1])
        s[x-1] = 1
    elif com == 'remove':
        x = int(line[1])
        s[x-1] = 0
    elif com == 'check':
        x = int(line[1])
        print(s[x-1])
    elif com == 'toggle':
        x = int(line[1])
        s[x-1] = int(not(s[x-1]))
    elif com == 'all':
        s = [1]*20
    elif com == 'empty':
        s = [0]*20