import sys
sys.stdin = open('./2022/inputfolder/2667.txt', 'r')

N = int(input())
map = [list(map(int, input())) for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]

dx, dy = [0,0,-1,1], [-1,1,0,0]
result = []

def dfs(i, j):
    global count
    visited[i][j] = 1 
    for w in range(4):
        nx = i + dx[w]
        ny = j + dy[w]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if map[nx][ny] == 0:
            continue
        if map[nx][ny] == 1 and visited[nx][ny] == 0:
            count += 1
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and map[i][j] == 1:
            count = 1
            dfs(i, j)
            result.append(count)

#print(map)
print(len(result))
result2 = sorted(result)
for i in range(len(result2)):
    print(result2[i])
