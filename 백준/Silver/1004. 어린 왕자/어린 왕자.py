import sys
T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    io = 0
    planetNum = int(input())
    for _ in range(planetNum):
        px, py, pr = map(int, sys.stdin.readline().split())
        distStart = ((x1-px)**2 + (y1-py)**2)**(1/2)
        distGoal = ((x2-px)**2 + (y2-py)**2)**(1/2)
        if (distGoal < pr) ^ (distStart < pr):
            io += 1
    print(io)
