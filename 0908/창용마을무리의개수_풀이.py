import sys
sys.stdin = open("s_input.txt", "r")

def dfs(cur): #cur : 현재 정점
    visited[cur] = True
    for i in range(1, N+1):
        if adj[cur][i] == 1 and not visited[i]:
           dfs(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)] # 인접행렬
    for i in range(M):
        u, v = map(int, input().split())
        # 무방향
        adj[u][v] = 1
        adj[v][u] = 1
    # for row in adj:
    #     print(row)
    #방문배열 생성
    visited = [False] * (N+1)
    #탐색 시작 횟수 저장 => 연결그래프의 갯수
    cnt = 0
    #모든 정점부터 dfs 탐색
    # 단 아직 방문 안한 곳에서만
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print("#{} {}".format(tc, cnt))