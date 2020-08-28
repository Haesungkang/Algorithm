dr = [-1, 0, 1, 0, 1, -1, 1, -1]
dc = [0, 1, 0 , -1, 1, -1, -1, 1]

def dfs(r,c,b): #현재좌표 r,c , color = b

    for k in range(8):
        nr = r
        nc = c
        count = 0
        while 0 <= nr < N and 0 <= nc < N:
            nr = nr + dr[k]
            nc = nc + dc[k]
            count += 1
        # 한방향으로 계속 전진하다가 같은 숫자를 만나면 그전까지 모든거 같은 숫자로 바꾸기
            if arr[nr][nc] == b:
                for _ in range(count):
                    nr -= dr[k]
                    nc -= dc[k]
                    arr[nr][nc] = b
                break

N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
arr[N // 2][N // 2 - 1] = 1
arr[N // 2 - 1][N // 2] = 1
arr[N // 2][N // 2] = 2
arr[N // 2 - 1][N // 2 - 1] = 2

for _ in range(M):
    j, i, c = map(int, input().split())
    print (i-1, j-1, c)
    arr[i-1][j-1] = c
    dfs(i-1,j-1,c)
    print(arr)


