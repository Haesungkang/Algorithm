import sys
sys.stdin = open('input.txt', 'r') # 파일로 인풋받기
T = 10
for tc in range(1, T+1):
    # 입력
    N = int(input()) # 빌딩의수
    arr = list(map(int,input().split())) # 입력받기
    # print(arr) 바로 주석처리하자
    # 계산
    view = 0 # 조망권수
    for i in range(2, N-2):
        left = arr[i-2] if (arr[i-2] > arr[i-1]) else arr[i-1] # 왼쪽빌딩중 높은 빌딩 찾기, 둘중 하나
        right = arr[i+1] if (arr[i+1] > arr[i+2]) else arr[i+2] # ctrl D로 복사
        t = left if (left > right) else right # 주변빌딩중 가장 높은 빌딩
        if arr[i] > t:
            view += (arr[i] - t)
        # 최대한 라이브러리 함수 안쓰기

    # 결과 출력
    print('#{} {}'.format(tc, view))

