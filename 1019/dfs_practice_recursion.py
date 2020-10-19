'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(N+1):
        if G[v][i] == 1 and visited[i] == 0:
            dfs(i)


N, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0]* (N+1)

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)