import math

T = int(input())
callFee = {}
names = []
times = []
for _ in range(T):
    time, name = map(str, input().split())
    h, m = map(int, time.split(":"))

    callTime = (h*60)+m
    if(name not in names):
        names.append(name)
        times.append(callTime)
    else:
        times[names.index(name)] += callTime

for i, j in zip(names, times):
    if(j >= 100):
        fee = math.ceil((j-100)/50)*3+10
    else:
        fee = 10
    callFee[i] = fee

nameSort = sorted(callFee)
res = sorted(nameSort, key = lambda x : callFee[x], reverse=True)

for i in res:
    print(i, callFee[i])

