import sys
sys.stdin = open("input_1.txt", "r")

def dfs(v): #현재 정점: v
    visited[v] = True
    for n in adj[v]:
        if not visited[v]:
            dfs(n)
    #방문하고 돌아올때마다 append
    S.append(n)

for tc in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adj = [[] for i in range(V+1)]    # 인접리스트 생성
    visited = [False] * (V+1)   #방문배열
    indeg = [0] * (V+1) #각 정점의 진입차수 저장
    S = []  #방문한 정점 저장

    for i in range(0, E):
        u, v = edges[i*2], edges[i*2+1] # 시작정점, 끝정점
        adj[u] .append(v)   # 유향그래프 -> 시작 -> 끝만 표현
        indeg[v] += 1   #끝 정점의 진입차수 증가시킴
    # print(adj)
    for i in range(1, V+1): #정점을 순회함
        if indeg[i]: continue #해당정점에 진입하수가 있으면 순회안함
        dfs(i)  #아니라면 => 미리 처리할 작업이 없음
    print("#{}".format(tc), end=" ")
    print(*S[::-1]

