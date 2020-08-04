T = 10
M = 100
for tc in range(1, T+1):
    N = int(input())    #덤프횟수
    arr = list(map(int,input().split()))

    for i in range(N): #덤프횟수만큼 반복
        #최소, 최대, 최소인덱스, 최대인덱스 저장
        max = 0
        min = 100000
        maxIdx = 0
        minIdx = 0
        for j in range(M):  # 상자를 가로 방향으로 순회
            if max < arr[j]:  #최대높이의 상자,위치 찾기
                max = arr[j]
                maxIdx = j
            if min > arr[j]: #최소높이의 상자, 위치찾기
                min = arr[j]
                minIdx = j
            arr[maxIdx] -= 1
            arr[minIdx] += 1 #최대최소높이에서 각각 +1,-1

        #덤핑을 끝내고 최대,최소 찾기
        max = 0
        min = 10000
        for i in range(M):
            if max < arr[i] : max = arr[i]
            if min > arr[i] : min = arr[i] #minmax함수를 쓴다면은 위치를 알수가 없다
    cnt = max - min
    print('#{} {}'.format(tc,cnt))