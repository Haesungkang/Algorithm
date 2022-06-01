import sys
sys.stdin = open("sample_input_3.txt", "r")

def dfs(sr, sc):
    # 시계방향 탐색을 위한 델타
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    s = [] # 스택
    s.append([sr,sc]) # 탐색 시작점(좌표) 스택에 넣기
    while len(s) != 0:  # 스택이 비어있지 않는 동안
        n = s.pop()
        #새로운 탐색좌표 계산 (사방 탐색)
        for k in range(4):
            nr = n[0] + dr[k]
            nc = n[1] + dc[k]
            if nr >= 0 and nr < N and nc >= 0 and nc < N: #미로 안이면
                if arr[nr][nc] == 3: #도착점인지 찾기
                    return 1    #찾음을 리턴
                elif arr[nr][nc] == 0:
                    s.append([nr,nc])
                    arr[nr][nc] = 1

    return 0


T =int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]
    # for row in arr:
    #     print(row)
    sr, sc = 0,0 # 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sr, sc = i, j
    #print(sr, sc)
    print("#{} {}".format(tc,dfs(sr,sc)))