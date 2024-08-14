'''import itertools

n = int(input())
sequence = list(map(int, input().split()))
x = int(input())

com = [itertools.combinations(sequence, 2)]

cnt = 0

for i in range(len(com)):
    if sequence.index(com[i][0]) < sequence.index(com[i][1]) and com[i][0] + com[i][1] == x:
        cnt += 1

print(cnt)'''
'''
n = int(input())
seq = list(map(int, input().split()))
x = int(input())

cnt = 0

for i in range(n):
    for j in range(i, n):
        if seq[i] + seq[j] == x:
            cnt += 1

print(cnt)'''

from itertools import combinations
import sys

n = int(input())
seq = list(map(int, sys.stdin.readline().split()))
x = int(input())

cnt = 0

for i in combinations(seq, 2):
    if sum(i) == x:
        cnt += 1

print(cnt)