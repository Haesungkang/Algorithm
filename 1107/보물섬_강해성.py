import sys
sys.stdin = open('input3.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def search(i, j, cnt):
    global shortcut
    # if cnt > shortcut:
    #     shortcut = cnt
    q = []
    q.append([i,j,0])

    while q:
        i, j, cnt = q.pop(0)
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr >= M or nc < 0 or nc >= N: continue
            if arr[nr][nc] == "W": continue
            if arr[nr][nc] == "L" and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append([nr, nc, cnt+1])
        if cnt > shortcut:
            shortcut = cnt

M, N = map(int, input().split())
arr = []
shortcut = 0
for _ in range(M):
    arr.append(list(input()))
# print(M, N)
# print(arr)
for i in range(M):
    for j in range(N):
        if arr[i][j] == "L":
            visited = [[0]*N for _ in range(M)]
            visited[i][j] = 1
            search(i, j, 0)

print(shortcut)