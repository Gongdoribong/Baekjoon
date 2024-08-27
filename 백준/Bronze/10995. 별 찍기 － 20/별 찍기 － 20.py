n = int(input())
flag = False
for i in range(n):
    if flag:
        print(' ',end='')
    print(('* '*n).rstrip())
    flag = not(flag)

