def factorial(n):
    if n == 1:
        return n
    if n == 0 :
        return 1
    return n*factorial(n-1)

T = int(input())
for t in range(T):
    bridge = input().split(' ')
    bridge = list(map(int, bridge))
    N = bridge[0]
    M = bridge[1]
    print(factorial(M)//(factorial(M-N)*factorial(N)))

