num = {"R":0, "P":1, "S":2}
ML, MR, TL, TR = map(str, input().split(" "))

M = [num[ML], num[MR]]
T = [num[TL], num[TR]]

win = [0, 0, 0, 0]
c = 0

for i in M:
    for j in T:
        n = i - j
        if (n==1 or n==-2):
            win[c] = 1
        elif (n==-1 or n==2):
            win[c] = -1
        c += 1

if(win[0]>0 and win[1]>0) or (win[2]>0 and win[3]>0):
    print("MS")
elif(win[0]<0 and win[2]<0) or (win[1]<0 and win[3]<0):
    print("TK")
else:
    print("?")
