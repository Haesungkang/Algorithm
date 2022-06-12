import sys
from collections import deque
sys.stdin = open('./2022/inputfolder/7569.txt', 'r')

M, N, H = map(int, input().split())
arr = [[ list(map(int, input().split())) for _ in range(N)] for i in range(H)]

#print(arr)
# 3차원 배열 표현 방법
queue = deque()
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [1,-1,0,0,0,0]

for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 1:
                queue.append((x,y,z))
def bfs():
    while queue:
        a,b,c = queue.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H:
                continue
            if arr[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[c][a][b] + 1
                queue.append((nx,ny,nz))
                #visited의 위치를 잘 파악하기
                visited[c][a][b] = 1

bfs()
print(arr)
result = 0 
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 0:
                result = -1
                print(-1)
                #프로그램 전체를 종료할때 쓰는것
                exit()
            if arr[z][x][y] >= result:
                result = arr[z][x][y]

if result > 0:
    print(result-1)

