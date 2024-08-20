import sys
while(True):
    p = int(sys.stdin.readline())
    if p == 0:
        break
    rng = sys.stdin.readline().split(',')
    book = [0]*(p+1)
    
    for i in rng:
        if('-' not in i):
            i = int(i)
            if(i<=p):
                book[i] = 1
        else:
            low, high = map(int, i.split('-'))
            if low > high:
                continue
            else:
                high += 1
                if(high>p):
                    book[low:] = [1]*len(book[low:])
                else:
                    book[low:high] = [1]*len(book[low:high])
    print(book.count(1))

