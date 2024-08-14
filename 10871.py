N, X = map(int, input().split())
num = list(map(int, input().split()))

'''
res = [i for i in num if i < X]

for t in res:
    print(t, end=" ")
'''

for i in num:
    if i < X :
        print(i, end=" ")

