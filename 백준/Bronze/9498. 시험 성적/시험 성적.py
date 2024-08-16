grade = int(input())
n = grade//10

if(n==10 or n==9):
    print('A')
elif(n==8):
    print('B')
elif(n==7):
    print('C')
elif(n==6):
    print('D')
else:
    print('F')
    