a=[]
for i in range(10):
    a.append(int(input()))
b=[]
for i in range(0,10):
    a[i]=a[i]%42
for j in a:
    if j not in b:
        b.append(j)
print(len(b))