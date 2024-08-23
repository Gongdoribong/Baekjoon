import sys
N, M = map(int, input().split())
memo = {}
for _ in range(N):
    site, pw = map(str, sys.stdin.readline().split())
    memo[site] = pw

for _ in range(M):
    siteFind = sys.stdin.readline().rstrip('\n')
    print(memo[siteFind])
