import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int,input().split())) for _ in range(5)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for i in range(0, len(arr)):
    # print(arr[i])
    for j in range(0, len(arr[i])):
        # print(arr[i][j])
        # 나의 현재 좌표 : i,j
        sum = 0 # 누적합
        for k in range(4): # 현재위치
            nr = i + dr[k] # 현재위치에서 추가하고자하는곳 추가하기
            nc = j + dc[k] # 새로운 좌표계산 등등
            # 새로운 좌표가 범위를 벗어나면 스킵
            if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr): continue
            # 계산 -> 이웃한 요소와의 차의 절대값
            # print(arr[i][j] - arr[nr][nc])
            sum += abs(arr[i][j] - arr[nr][nc]) #print를 빼는거 주의하기
        print(sum, end=' ')
    print()




