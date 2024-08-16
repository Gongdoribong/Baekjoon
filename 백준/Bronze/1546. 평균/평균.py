T=int(input())
a=list(map(int, input().split(" ")))
M=max(a)
for i in range(T):
    a[i]=a[i]/M*100
print(sum(a)/T)