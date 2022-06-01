def dfs(i, product):
    global result

    if i == N:
        if product < result:
            result = product
            return

    if product > result:
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(i + 1, product + arr[i][j])
                visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 999999

    dfs(0, 0)
    print("#{} {}".format(tc, result))