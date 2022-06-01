'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):

    visited[v] = 1
    print(v, end=" ")
    for w in range(N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(v):
    visited[v] = 1
    Q = []
    Q.append(v)
    while Q:

        v = Q.pop(0)
        for w in range(N + 1):
            if G[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
                # bfs(w)

N, E = map(int, input().split())
temp = list(map(int, input().split()))
# print(N, E)
# print(temp)
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

# for i in G:
#     print(i)
dfs(1)