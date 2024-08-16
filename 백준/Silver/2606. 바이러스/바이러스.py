def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

n=int(input())
v=int(input())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(v):
    a,b=map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(1)
print(sum(visited)-1)