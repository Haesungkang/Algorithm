import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    stack = []

    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                stack.append(1)
            if arr[i][j] == 0 and len(stack) == K:
                result += 1
                stack = []
            if arr[i][j] == 0 and len(stack) != K:
                stack = []
        if len(stack) == K:
            result += 1
        stack = []

    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                stack.append(1)
            if arr[i][j] == 0 and len(stack) == K:
                result += 1
                stack = []
            if arr[i][j] == 0 and len(stack) != K:
                stack = []
        if len(stack) == K:
            result += 1
        stack = []



    print("#{} {}".format(tc, result))
