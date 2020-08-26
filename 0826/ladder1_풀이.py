import sys
sys.stdin = open("input.txt","r")

def search(r,c):    #r: row, c: column
    #왼 오 아래
    dr = [0,0,1]
    dc = [-1,1,0]
    num = ladder[r][c]
    visited = [[0 for _ in range(N)] for _ in range(N)] # 방문배열 생성
    visited[r][c] = 1

    while True:
        if num == 2: return True #찾음을 리턴
        if r == 99 : return False #못찾음을 리턴

        for k in range(3):
            # 새로운 좌표 구하기
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위를 벗어나지 않는지? 이미 방문했는지?
            if nr < 0 or nr >= N or nc<0 or nc >= N: continue
            if ladder[nr][nc] == 0: continue
            if visited[nr][nc] == 1: continue
            r = nr #새로운좌표로 현위치를 갱신
            c = nc
            num = ladder[nr][nc]
            visited[nr][nc] = 1 #방문표시
            break # 갈길을 찾았으면 탐색을 종료하고 반복을 빠져나감

T = 10
for tc in range(1, T+1):
    N = 100
    int(input()) # tc 제거용
    ladder = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if ladder[0][i] == 1: #0행을 순회하면서 1인 곳을 찾아서 시작
            result = search(0, i) # 좌표넘겨주고 탐색 => True 또는 False 리턴
        if result:
            cnt = i
            break
    print("#{} {}".format(tc, cnt))
