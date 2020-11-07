import sys
sys.stdin = open('sample_input.txt', 'r')

# 1 상하좌우
# 2 상하
# 3 좌우
# 4 상우
# 5 하우
# 6 하좌
# 7 상좌

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상, 하, 좌, 우 0,1,2,3,
# 하, 상, 우, 좌 1,0,3,2

## 그숫자에 따른 상하좌우 TF를 설정해서
## 다음으로 진행할때 -> 상으로 갈려하는데 그때 다음값이 상이 T가 되면 움직이기

fixture = [1, 0, 3, 2]

def findnumber(n):
    if n == 1:
        q = [True,True,True,True]
        return q
    elif n == 2:
        q = [True,True,False,False]
        return q
    elif n == 3:
        q = [False,False,True,True]
        return q
    elif n == 4:
        q = [True,False,False,True]
        return q
    elif n == 5:
        q = [False,True,False,True]
        return q
    elif n == 6:
        q = [False,True,True,False]
        return q
    elif n == 7:
        q = [True,False,True,False]
        return q
    else:
        q= [False,False,False,False]
        return q


def dfs(r, c, l):
    global cnt, q

    while q:

        if l == L:
            return

        for _ in range(len(q)):
            xr, xc, num = q.pop(0)
            visited[xr][xc] = 1
            for k in range(4):
                nr = xr + dr[k]
                nc = xc + dc[k]
                if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
                if arr[nr][nc] != 0 and visited[nr][nc] == 0:
                    if findnumber(num)[k] == True and findnumber(arr[nr][nc])[fixture[k]] == True:
                        if [nr,nc,arr[nr][nc]] not in q:
                            q.append([nr,nc,arr[nr][nc]])
                            cnt += 1
            #print(q)
        l += 1

T = int(input())
for tc in range(1, T+1):
    #세로가로 세로위치가로위치 시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = []
    # print(arr)
    # print(visited)

    visited[R][C] = 1
    q.append([R, C, arr[R][C]])
    cnt = 1
    dfs(R,C,1)
    print("#{} {}".format(tc, cnt))
    # for row in visited:
    #     print(row)
