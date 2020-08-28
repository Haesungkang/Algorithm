
import sys
sys.stdin = open("sample_input(1).txt", 'r')

# 사방탐색 - 시계방향으로(취향따라하기)
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
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        # 한방향으로 계속 전진하다가 같은 숫자를 만나면 그전까지 모든거 같은 숫자로 바꾸기
            if arr[nr][nc] == b:
                stack = []
                for _ in range(count):
                    nr -= dr[k]
                    nc -= dc[k]
                    stack.append(arr[nr][nc])
                if 0 in stack:
                    break
                else:
                    for _ in range(count):
                        nr += dr[k]
                        nc += dc[k]
                        arr[nr][nc] = b
                break


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2 - 1] = 2
    #print(arr)
    for _ in range(M):
        j, i, c = map(int, input().split())
        # print (i-1, j-1, c)
        arr[i-1][j-1] = c
        dfs(i-1,j-1,c)
        # print(arr)

    # print(arr)

    black_count =0
    white_count =0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black_count += 1
            if arr[i][j] == 2:
                white_count += 1

    print("#{} {} {}".format(tc, black_count, white_count))

