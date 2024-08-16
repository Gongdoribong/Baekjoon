while(True):
    s = list(input())
    if s == ["0"]:
        break
    flag = 0
    std = len(s)//2

    if int("".join(s))<10:
        print("yes")
        continue

    for i in range(len(s)//2):
        if len(s)%2 == 0 :  #짝수인경우
            if s[std-i-1] == s[std+i]:
                flag = 1
            else:
                flag = 0
                break
        else:   #홀수인경우
            if s[std-(i+1)] == s[std+(i+1)]:
                flag = 1
            else:
                flag = 0
                break

    if flag:
        print("yes")
    else:
        print("no")
