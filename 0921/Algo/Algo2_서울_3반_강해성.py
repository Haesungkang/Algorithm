# import sys
# sys.stdin = open("input1.txt", "r")

#상하좌우찾아주기
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

def search(R, C):
    global cnt, visited
    # 방문배열과 폭발력을 저장
    D = arr[R][C]
    visited[R][C] = 1
    #폭탄 개수 추가
    cnt += 1
    for k in range(4):
        #폭탄의 범위만큼 움직여주기
        for t in range(D):
            dR = R + dr[k] * (t+1)
            dC = C + dc[k] * (t+1)
            #범위 밖으로 벗어날 경우 out
            if dR >= N or dR < 0 or dC >= N or dC < 0: continue
            # 만약 폭탄을 방문하지 않았고 폭탄이 있을경우
            if visited[dR][dC] == 0 and arr[dR][dC] != 0:
                search(dR, dC)
            else:
                continue

    return

T = int(input())

for tc in range(1, T+1):
    #input넣어주기
    N = int(input())
    R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #방문배열 형성
    visited = [[0 for _ in range(N)] for _ in range(N)]
    #갯수
    cnt = 0

    search(R, C)
    print("#{} {}".format(tc,cnt))