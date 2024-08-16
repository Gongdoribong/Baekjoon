import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

TBundle = 0

for i in sizes:
    TBundle += math.ceil(i/T)

penBundle = math.floor(N/P)
penPiece = N%P

print(TBundle)
print(penBundle, penPiece)
