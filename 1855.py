col = int(input())
string = list(input())
l = len(string)

temp = []
decode = []

j = col

for i in range(j, l, col*2):
    string[i:i+col] = reversed(string[i:i+col])

for i in range(col):
    for j in range(i, l, col):
        decode.append(string[j])

print(''.join(decode))