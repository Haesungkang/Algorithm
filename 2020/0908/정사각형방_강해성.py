import sys
sys.stdin = open("input_3.txt", "r")
sys.setrecursionlimit(10**8)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, N, result): # r,c : 좌표, result

    result.append(arr[r][c])

    for k in range(4):
        nr = r + dr[k]  #새좌표 계산
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if arr[nr][nc] == arr[r][c] + 1:
            dfs(nr, nc, N, result)

    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    result = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # for row in arr:
    #     print(row)

    for i in range(N):
        for j in range(N):
            # 매 좌표마다 dfs탐색해서 result에 넣기
            countinglist=[]
            dfs(i, j, N, countinglist)
            result.append(countinglist)
            print(countinglist)
    #넣은 result기준으로 maxlength찾기
    max_l = 1
    start = 0
    for i in range(len(result)):
        if len(result[i]) > max_l:
            max_l = len(result[i])
            start = result[i][0]
        if len(result[i]) == max_l:
            if result[i][0] < start:
                start = result[i][0]
    print("#{} {} {}".format(tc, start, max_l))