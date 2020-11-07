import sys
sys.stdin = open('input2.txt', 'r')

dr = [0,0,1,-1,1,1,-1,-1]
dc = [1,-1,0,0,1,-1,1,-1]

def dfs(r, c):

    visited[r][c] = 1
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nc < 0 or nr >= H or nc >= W: continue
        if visited[nr][nc] == 1: continue
        if arr[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)


tc = True
while tc:
    W, H = map(int,input().split())
    if W == 0 or H == 0:
        tc = False
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i,j)
    print(cnt)