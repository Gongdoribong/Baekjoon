import sys
sys.setrecursionlimit(1000000000) #반복제한 늘리기

def dfs(now):
    global visit
    visit[now]=1    #나 자신을 추가해준다
    for i in m[now]:
        if visit[i]==-1:    #방문하지 않은 방문 가능 노드가 있다면
            visit[now]+=dfs(i)  #방문하며 그 노드의 서브트리 개수를 더해준다
    return visit[now]   #내 서브트리 개수를 리턴한다


N,R,Q=map(int,sys.stdin.readline().split(' '))

m=[[]for _ in range(N+1)]   #트리 표현
visit=[-1 for _ in range(N+1)]  #방문 및 서브트리 개수 표현

for _ in range(N-1):    #간선정보
    a,b=map(int,sys.stdin.readline().split(' '))
    m[a].append(b)
    m[b].append(a)

dfs(R)  #루트 노드부터 방문 시작
for _ in range(Q):  #쿼리
    get=int(sys.stdin.readline())
    print(visit[get])