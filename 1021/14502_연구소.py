import sys
sys.stdin = open('input2.txt', 'r')
sys.setrecursionlimit(100000)

from itertools import combinations

T = int(input())

#바이러스 전염시키기
def dfs(i, j):
    global visited
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    Q = []
    Q.append([i,j])
    while Q:
        i, j = Q.pop(0)
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr >= N or nc< 0 or nc >= M: continue
            if arr[nr][nc] == 1: continue
            if visited[nr][nc] == 1: continue
            if arr[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append([nr, nc])

            #visited[nr][nc] = 1


# zero 3개관련 함수
# def comb(n, r):  # n : 원소 인덱스, r : set 배열의 어디에 넣을지 (선택한 원소의 수 )
#     global selidx
#     if r == z:  # 조합 다고름
#         selidx += sel
#         return
#     elif n >= len(zeroidx):
#         return
#     sel[r] = zeroidx[n]
#     comb(n + 1, r + 1)  # r위치의 원소 선택한 경우
#     comb(n + 1, r)  # r위치의 원소 선택안함 -> 덮어씌우는거

        
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #print(visited)
    #print(arr)
    # zero값 모두 찾아주기
    zeroidx = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
               zeroidx.append([i,j])
    #zeroidx에서 조합 3개 해주기
    #print(zeroidx)
    # selidx=[]
    z = 3  # 선택할 조합의 개수
    sel = [0] * z  # 조합을 담을 배열
    selidx = list(combinations(zeroidx, 3))
    #print(selidx)
    resultlist = []
    for k in selidx:
        arr[k[0][0]][k[0][1]] = 1
        arr[k[1][0]][k[1][1]] = 1
        arr[k[2][0]][k[2][1]] = 1

        visited = [[0 for _ in range(M)] for _ in range(N)]

        # 바이러스 전염
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    dfs(i,j)

        # for row in arr:
        #     print(row)
        # print()
        result = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and visited[i][j] == 0:
                    result += 1


        resultlist.append(result)

        arr[k[0][0]][k[0][1]] = 0
        arr[k[1][0]][k[1][1]] = 0
        arr[k[2][0]][k[2][1]] = 0


    #print(resultlist)
    print(max(resultlist))
    #print(len(resultlist))



    # 일단 0에서 1을 설정한다
    # 0에서 1설정할때 했던것들은 1로 visited를 하던가 뭘하던가해야할듯?

    # 2를 drdc를 통해서 모두 0을 2로바꿔준다
    # 그다음에 0의 갯수를 출력한다

