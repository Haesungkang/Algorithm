import sys
sys.stdin = open('../0inputlist/sample_input_1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    #모든값들을 초기화 시키기
    result =0
    blank = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    for case in range(1, N+1):
        A, B, C, D, E = map(int, input().split())

        #빨간색일경우 blank에서 빨간색 칠하기
        if E == 1:
            for i in range(A, C+1):
                for j in range(B, D+1):
                    blank[i][j] += 1
        #파란색일경우 blank에서 파란색 칠하기
        if E == 2:
            for i in range(A, C+1):
                for j in range(B, D+1):
                    blank[i][j] += 2

    #두개중합쳤을때 3인경우 count해서 계산하기
    for i in range(10):
        for j in range(10):
            if blank[i][j] == 3:
                result += 1
    print('#{} {}'.format(tc, result))


