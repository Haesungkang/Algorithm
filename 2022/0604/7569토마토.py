import sys
from collections import deque
sys.stdin = open('./2022/inputfolder/7569.txt', 'r')

M, N, H = map(int, input().split())
arr = [[ list(map(int, input().split())) for _ in range(N)] for i in range(H)]

print(arr)
# 3차원 배열 표현 방법
queue = deque()
dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [1,-1,0,0,0,0]

for z in range(H):
    for y in range(M):
        for x in range(N):
            if arr[z][y][x] == 1:
                queue.append((x,y,z))
def bfs(a):
    pass
