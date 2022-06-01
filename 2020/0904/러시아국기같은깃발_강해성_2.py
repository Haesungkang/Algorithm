import sys
sys.stdin = open("sample_input_1.txt", "r")

T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[i for i in input()] for _ in range(N)]
    ans = 0
    # default
    # for i in range(M):
    #     if arr[0][i] != 'W':
    #         ans += 1
    #         arr[0][i] = "W"
    # for i in range(M):
    #     if arr[N - 1][i] != 'R':
    #         ans += 1
    #         arr[N - 1][i] = 'R'

    #0 white
    #1 ~ i-1 white
    #i ~ j-1 blue
    #j ~ N-2 red
    #N-1 red
    min = 9999
    for i in range(1, N-1):
        for j in range(i+1, N):
            cnt = 0
            for W in range(i):
                for k in range(M):
                    if arr[W][k] != "W":
                        cnt +=1
            for B in range(i, j):
                for k in range(M):
                    if arr[B][k] != "B":
                        cnt += 1
            for R in range(j, N):
                for k in range(M):
                    if arr[R][k] != "R":
                        cnt +=1
            if cnt < min:
                min = cnt

    print("#{} {}".format(tc, min))


