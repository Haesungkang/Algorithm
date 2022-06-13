import sys
from collections import deque
sys.stdin = open('./2022/inputfolder/2574.txt', 'r')

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
#print(arr)

dc, dr = [0,0,-1,1], [1,-1,0,0]
result = 0
# def melt(x, y):
#     cnt = 0
#     for i in range(4):
#         nx = x + dc[i]
#         ny = y + dr[i]
#         if nx < 0 or nx > n or ny > m or ny < 0:
#             continue
#         if arr[nx][ny] == 0:
#             cnt += 1
#     visited[x][y] = cnt

def meltingtime():
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dc[k]
                    ny = j + dr[k]
                    if nx < 0 or nx > n or ny > m or ny < 0:
                        continue
                    if arr[nx][ny] == 0:
                        cnt += 1
                visited[i][j] = cnt
                arr[i][j] = arr[i][j] - visited[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0

island = 0
queue = deque()

visitis = [[0] * m for _ in range(n)]
cnt = 1

def start(i, j, cnt):
    visitis[i][j] = cnt
    for x in range(4):
        ni = i + dc[x]
        nj = j + dr[x]
        if ni < 0 or ni > n or nj > m or nj < 0:
            continue
        if arr[ni][nj] > 0 and visitis[ni][nj] == 0:
            start(ni, nj, cnt)

def counting():
    global cnt 
    cnt = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visitis[i][j] == 0:
                cnt += 1
                start(i, j, cnt)


timer = 0
timer1 = False
for i in range(10):
    timer += 1
    meltingtime()
    visitis = [[0] * m for _ in range(n)]
    counting()
    if cnt >= 4:
        timer1 = True
        print(timer)
        break

if timer1 == False:
    print(0)


