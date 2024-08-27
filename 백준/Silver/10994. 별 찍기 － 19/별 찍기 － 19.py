n = int(input())

ceil = (4*n)-3
fill = ceil-4
print('*' * ceil)

if fill>0:
    while(True):
        wall = (ceil-fill)//4
        print('* '*wall + ' '*fill + ' *'*wall)
        if fill == 1:
            break
        print('* '*wall + '*'*fill + ' *'*wall)
        fill -= 4

    while(True):
        wall = (ceil-fill)//4
        print('* '*wall + '*'*fill + ' *'*wall)
        print('* '*wall + ' '*fill + ' *'*wall)
        if (fill+4) == ceil:
            print('*'*ceil)
            break
        fill += 4
