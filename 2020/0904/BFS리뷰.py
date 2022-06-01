'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# pop(0)와 append로 queue를 조작한다는 느낌을 생각하자
#관통형 원기둥을 생각하고 first in first serve 느낌으로

#너비우선탐색(BFS)
def bfs(v): # 시작정점
    # 큐 생성
    q =[]
    # 방문배열을 생성
    visited = [0] * (V+1)
    # 시작정점을 위해 큐에 넣음
    q.append(v)
    # 시작정점을 방문했다고 표시
    visited[v] = 1
    # 여기파트에서만 반복이 될예정이기때문에 방문배열생성은 위에서 생성해도 무방하다

    # 큐가 빌떄까지 반복
    while q:
        # 큐에서 정점을 하나로 꺼내옴
        n = q.pop(0)
        # n에 인접한 정점중 아직 방문하지 않은 정점 u을 큐에 넣음
        for u in range(1, V+1):
            if adj[n][u] == 1 and visited[u] == 0:
                # 정점 u를 큐에 넣고
                q.append(u)
                 # 정점 u를 방문했다고 표시
                visited[u] = visited[n] + 1

V,E = map(int,input().split())
edges = list(map(int,input().split()))

adj = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edges[2*i], edges[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 #무방향이니깐

bfs(1) #시작정점이 1