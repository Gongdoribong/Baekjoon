cnt = [0]*26
s = list(input())

even = 0
odd = 0
for i in s:
    n = s.count(i)
    if n%2 == 0: #짝수면
        even = 1
    else:
        odd = 1

if even and odd:
    print(2)
elif even:
    print(0)
elif odd:
    print(1)

