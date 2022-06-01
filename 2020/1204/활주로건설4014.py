import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr, N, X)

    cnt = 0
    #가로 체크

    print(tc, cnt)

    #세로 체크
    # for j in range(N):
    #     for i in range(N-1):
    #         pass


    # counting = True
    # for i in range(N):
    #     for j in range(N-1):
    #         if arr[i][j] - arr[i][j+1] == 1:
    #             for k in range(2, X+1):
    #                 if arr[i][j+1] != arr[i][j+k]:
    #                     counting = False
    #             if counting:
    #                 cnt += 1
    #                 break
