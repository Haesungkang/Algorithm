# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    #testcase관련 N,M,K,arr 모두 받기
    N, M, K = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #도넛합에 대한 result추가
    result = []
    for i in range(N-K+1):
        for j in range(M-K+1):
            donut = 0
            #도넛의 맨위와 맨아래부분은 전부 추가해야한다
            donut += sum(arr[i][j:j+K])
            donut += sum(arr[i+K-1][j:j+K])
            #가운데부분은 맨처음과 맨끝만 추가해준다
            for t in range(1, K-1):
                donut += arr[i+t][j]
                donut += arr[i+t][j+K-1]
            #리스트를 result에 추가해준다
            result.append(donut)
    #출력형식에 맞게 출력하기
    print("#{} {}".format(tc, max(result)-min(result)))

