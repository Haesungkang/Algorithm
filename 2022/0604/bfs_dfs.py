import sys
sys.stdin = open("2022/0601/inputfolder/bfsinput.txt", "r")

def dfs(v):
    
    visited[v] = 1
    
    print(v, end=" ")
    for w in range(N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(v):
    visited = [0] * (N+1)
    visited[v] = 1
    
    Q = []
    Q.append(v)
    while Q:
        v = Q.pop(0)
        for w in range(N+1):
            if G[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
                print(w, end=" ")

N, E = map(int, input().split())
temp = list(map(int, input().split()))

visited = [0] * (N+1)
G = [[0] * (N+1) for _ in range(N+1)]


for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = G[e][s] = 1

for i in range(1, N+1):
    print("{} {}".format(i, G[i]))

print("dfs start")
dfs(1)
print("bfs start")
bfs(1)