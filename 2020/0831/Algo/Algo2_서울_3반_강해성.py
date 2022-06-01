
# 상하좌우를 움직일 예정
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    # 입력받은 행렬 0으로 전부 만들어주기
    arr = [[0 for _ in range(M)] for _ in range(N)]
    # 입력받은 좌표에 대한 행렬 표시 시키기
    for k in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1

    count = 0
    # for문을 이용해서 먼저 1의 위치를 찾습니다
    for i in range(N):
        for j in range(M):
            # 만약에 1인 행렬을 찾았을경우
            if arr[i][j] == 1:
                arr[i][j] = 0
                count += 1
                # 찾은 행렬에서 좌우 탐색하면서 0을 지워나갑니다
                while 0 <= i < M and 0 <= j < N:
                    falsecount = 0
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        # boundary 설정
                        if nr >= M or nr < 0 or nc < 0 or nc >= N:
                            falsecount += 1
                            continue
                        # 1값을 찾아낼경우 그지점으로 다시 지정하여 while문을 돌려줍니다
                        if arr[nr][nc] == 1:
                            arr[nr][nc] = 0
                            i = nr
                            j = nc
                            break
                        if arr[nr][nc] == 0:
                            falsecount += 1
                        # 만약에 상하좌우가 모두 0인경우가 발생할경우 while문에서 빠져나갑니다
                        if falsecount == 4:
                            break
                    if falsecount == 4:
                        break
    # dfdfdfdf
    print("#{} {}".format(tc, count))




