n=[]
for _ in range(9):
    n.append(int(input()))
    
print(max(n))
print(n.index(max(n))+1)
