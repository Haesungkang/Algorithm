import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(i,j):
    global q

    while q:

        i, j = q.pop(0)
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue

            counting = int(arr[nr][nc])
            if visited[nr][nc] > visited[i][j] + counting:
                visited[nr][nc] = visited[i][j] + counting
                q.append([nr, nc])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[99999999] * N for _ in range(N)]
    visited[0][0] = 0
    q =[[0,0]]
    bfs(0,0)
    print("#{} {}".format(tc,visited[N-1][N-1]))