a = list(input())
b = list(input())

a_alpha = [0]*26
b_alpha = [0]*26

for i, j in a, b:
    a_alpha[ord(i)-97] += 1
    b_alpha[ord(j)-97] += 1

