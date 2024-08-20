s = list(input())
a = ['a', 'e', 'i', 'o', 'u']

sum = 0

for i in a:
    sum += s.count(i)

print(sum)