import sys
sys.stdin = open('input.txt', 'r')

dr = [0,0,1,-1]
dc = [-1,1,0,0]

def dfs(r, c):
    global cnt
    visited[r][c] = cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
        if visited[nr][nc] == 0 and arr[nr][nc] == 1:
            cnt += 1
            dfs(nr, nc)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
q =[]
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            dfs(i,j)
            result.append(cnt)

# for row in visited:
#     print(row)
finalresult = sorted(result)
print(len(result))
for i in finalresult:
    print(i)