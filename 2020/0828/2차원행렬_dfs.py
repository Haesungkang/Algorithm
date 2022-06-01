'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

# 사방탐색 - 시계방향으로(취향따라하기)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0 , -1]

def dfs(r,c): #현재좌표 r,c
    arr[r][c] = 2
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if arr[nr][nc] == 0 or arr[nr][nc] == 2: continue #계속 무한반복을 방지하기위해 or 뒷부분을 넣어준다
        # 재귀는 같은 행동을 반복할때하는것
        dfs(nr, nc) # dfs(0,1) -> dfs(0,2) -> dfs(1,2)
        # 함수가끝나면 내가 부른곳으로 간다
        # 그래서 결국 다채워지면 처음 지점으로 돌아간다

N = int(input())
arr = [ list(map(int,input())) for _ in range(N)]
# for row in arr:
#     print(row)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i,j) # dfs탐색 시작

for row in arr:
    print(row)

