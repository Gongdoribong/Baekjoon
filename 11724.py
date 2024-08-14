import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
# 인접 리스트 -> 인덱스를 그대로 정점의 번호로 사용
graph = list([] for _ in range(N+1))

# 연결 요소 개수
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실시
visited = [0] * (N+1)
def dfs(v):
    visited[v] = 1

    for node in graph[v]:
        if not visited[node]:
            dfs(node)


cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)