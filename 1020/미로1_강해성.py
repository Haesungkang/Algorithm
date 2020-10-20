import sys
sys.stdin = open("input.txt", "r")

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,tc):
    global result
    maze[r][c] = 2
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= 16 or nc < 0 or nc >= 16 : continue
        if maze[nr][nc] == 1 or maze[nr][nc]== 2: continue
        if maze[nr][nc] == 3:
            result = 1
        dfs(nr,nc,tc)

for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                dfs(i,j,tc)
    print("#{} {}".format(tc,result))