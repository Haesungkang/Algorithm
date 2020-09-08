import sys
sys.stdin = open("input_3.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, -1, 0]
def dfs(r,c,cnt):   # 현재좌표, 거리
    #마지막에만 호출해버리고 싶으면 변수를 하나만들어서 그때 호출시키면된다
    global dist
    if dist < cnt:
        dist = cnt
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if mat[nr][nc] == mat[r][c] + 1:
            dfs(nr, nc, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # for row in mat:
    #     print(row)
    cnt1 = 0
    maxr = maxc = 0
    for r in range(N):
        for c in range(N):
            dist = 0
            dfs(r,c,1)  #시작 좌표(r,c), 거리
            if cnt1 < dist:
                cnt1 = dist
                maxr = r
                maxc = c
            elif cnt1 == dist and mat[r][c] < mat[maxr][maxc]:
            # 거리가 같을 경우 -> 방에 적힌 값이 작을때만 갱신
                maxr = r
                maxc = c

    print("#{} {} {}".format(tc, mat[maxr][maxc], cnt1))