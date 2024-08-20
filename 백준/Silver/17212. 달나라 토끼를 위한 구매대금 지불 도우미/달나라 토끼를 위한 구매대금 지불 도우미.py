N = int(input())

if(N!=3 and N%7 == 3):
    tri = N//7 - 1
    N = (N%7) + 7
else:
    tri = N//7
    N = (N%7)
tri += N//5
N = (N%5)
tri += N//2
N = (N%2)
tri += N//1

print(tri)
