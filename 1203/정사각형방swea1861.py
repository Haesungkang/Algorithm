import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def search(starti, startj, i, j, cnt):

    global maxroom, maxstart
    q = []
    q.append([starti, startj, i, j, cnt])

    while q:
        starti, startj, i, j, cnt = q.pop(0)

        if cnt > maxroom:
            maxroom = cnt
            maxstart = arr[starti][startj]

        if cnt == maxroom:
            if arr[starti][startj] <= maxstart:
                maxstart = arr[starti][startj]
                maxroom = cnt


        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr >=N or nc >= N or nc < 0: continue
            if visited[nr][nc] == 1: continue
            if arr[i][j] + 1 == arr[nr][nc]:
                visited[nr][nc] = 1
                q.append([starti, startj, nr, nc, cnt+1])


for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    maxroom = 0
    maxstart = 0
    # print(arr)
    for i in range(N):
        for j in range(N):
            visited = [[0]*N for _ in range(N)]
            visited[i][j] = 1
            search(i, j, i, j, 1)

    print("#{} {} {}".format(tc, maxstart, maxroom))