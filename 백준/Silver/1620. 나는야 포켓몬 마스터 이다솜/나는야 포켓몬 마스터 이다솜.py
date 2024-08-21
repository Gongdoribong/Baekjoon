import sys
N, M = map(int, input().split())
pokeList = {}
pokeOrder = {}
for i in range(N):
    poke = sys.stdin.readline().rstrip('\n')
    pokeList[i] = poke
    pokeOrder[poke] = i

for i in range(M):
    q = sys.stdin.readline().rstrip('\n')
    if q[0] in '123456789':
        print(pokeList[int(q)-1])
    else:
        print(pokeOrder[q]+1)
