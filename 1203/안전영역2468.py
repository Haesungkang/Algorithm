import sys
sys.stdin = open('input2.txt', 'r')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def search(i,j):

    global maxwidth

    q= []
    q.append([i,j])
    while q:
        i, j = q.pop(0)
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nc < 0 or nr >= N or nc >= N : continue
            if visited[nr][nc] == 1: continue
            if arr[nr][nc] > maxwidth:
                visited[nr][nc] = 1
                q.append([nr, nc])
    return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#song에게 배운것 아무것도 없을때 minimum값을 설정해야한다
maxcnt = 1
maxwidth = 0


for a in arr:
    if maxwidth < max(a):
        maxwidth = max(a)-1

while maxwidth > 0:

    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > maxwidth and visited[i][j]== 0:
                visited[i][j] = 1
                cnt += 1
                search(i,j)

    if maxcnt < cnt:
        maxcnt = cnt

    maxwidth -= 1

print(maxcnt)
