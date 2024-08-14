words = list(input())
alpha = [0]*26
for i in words :
    alpha[ord(i) - 97] += 1

print(*alpha)