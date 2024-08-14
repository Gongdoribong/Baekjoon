N = int(input())
for _ in range(N):
    ori, strfry = input().split()
    ori = sorted(list(ori))
    strfry = sorted(list(strfry))

    if(ori == strfry):
        print("Possible")
    else:
        print("Impossible")
