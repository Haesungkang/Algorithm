import sys
sys.stdin = open('../0inputlist/input2.txt', 'r')
'''

# 1. 길이가 M인 구간에서의 시작 인덱스

N = 5인 경우의 인덱스 범위 : 0 ~ 4
M = 3인 경우 
012,123,234,345(인덱스범위가 초과하므로 안된다)

i (반복계수) : 0~2 : 0 ~ 5 -3 --> 0 ~ (N - M)으로 범위를 잡으면 된다
'''

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(N,M)
    # print(arr)
    #for문 밖에서 min,max를 초기화시킨다
    Min = 10000 * M #아주큰값설정
    Max = 0
    for i in range(N - M + 1): # M개의 구간을 시작하기 위한 인덱스
        sum = 0 # 구간합을 구하기위한 변수
        # print(arr[i], end=' ')
        for j in range(M):  # M이 3인경우 j -> 0,1,2
            # print(arr[i+j], end=' ')
            sum += arr[i+j]
        if sum < Min:
            Min = sum
        if sum > Max:
            Max = sum
    # print(Max, Min)
    print("#{} {}".format(tc,(Max-Min)))





