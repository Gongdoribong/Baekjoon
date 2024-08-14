asc = [x for x in range(1, 9)]
desc = list(reversed(asc))
scale = list(map(int, input().split(" ")))

if scale == asc:
    print("ascending")
elif scale == desc:
    print("descending")
else:
    print("mixed")
