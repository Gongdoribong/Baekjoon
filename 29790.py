b, u, l = map(int, input().split())
cnt = 0
if b>=1000 and (u>=8000 or l>=260):
    print("Very Good")
elif b>=1000:
    print("Good")
else:
    print("Bad")
    