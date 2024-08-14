from math import sqrt

dots = input().split(" ")
dots = list(map(int, dots))

'''
Xa = dots[0]
Ya = dots[1]
Xb = dots[2]
Yb = dots[3]
Xc = dots[4]
Yc = dots[5]

거리 공식 : 루트 x-x제곱 + y-y제곱

방법 1. 거리가 제일 좁은데가 최대, 넓은데가 최소.... 패스할까?
'''

distance = []
distance.append(sqrt((dots[0]-dots[2])**2 + (dots[1]-dots[3])**2))
distance.append(sqrt((dots[0]-dots[4])**2 + (dots[1]-dots[5])**2))
distance.append(sqrt((dots[2]-dots[4])**2 + (dots[3]-dots[5])**2))

distance.index(max(distance))