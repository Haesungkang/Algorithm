import sys
sys.stdin = open("input.txt", "r")
# test case 입력받기
T = int(input())
# 각각의 test case마다
for tc in range(1, T+1):
    # 입력값 input 받기
    N, M, D = map(int, input().split())
    # 0으로 이뤄진 빈 2차원 행렬 생성
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # print(arr)
    # 가운데값 생성
    middle = N//2
    arr[middle][middle] = M
    # print(arr)
    # 맨위부터 숫자를 채워나가는 방법 : 횟수는 middle값기준으로
    for k in range(middle+1):
        # 각각 행렬에 규칙을보면 양쪽으로 하나씩 줄어든다 그래서 그만큼 채워준다
        for i in range(N- 2*k):
            for j in range(N - 2*k):
                # 숫자가 규칙적으로 줄어들기위한 방법
                arr[i+k][j+k] = M + (D *(middle-k))

    # for row in arr:
    #     print(row)
    # 행별 합을 저장하기위한 result 생성
    result = []
    # result 각각 더해준다
    for row in arr:
        result.append(sum(row))
    # result값을 출력형식에 맞게 변형시켜 출력
    print("#{}".format(tc), end=" ")
    for i in result:
        print(i, end=" ")
    print()