import sys
sys.stdin = open('./2022/inputfolder/2606.txt', 'r')

C = int(input())
N = int(input())
G = [[0] * (C+1) for _ in range(C+1)]
for i in range(N):
    a, b = map(int, input().split())
    G[a][b] = G[b][a] = 1

visited = [0] * (C+1)


def dfs(v):
    global cnt
    visited[v] = 1
    for w in range(C+1):
        if G[v][w] == 1 and visited[w] == 0:
            cnt += 1
            dfs(w)

cnt = 0
dfs(1)
print(cnt)


