import sys
sys.stdin = open("s_input.txt", "r")

def dfs(v, result):

    if visited[v] == 1:
        pass
    else:
        visited[v] = 1
        result.append(v)

        for w in range(1, N+1):
            if arr[v][w] == 1 and visited[w] == 0:
                dfs(w, result)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0] * (N + 1)
    result2 = []
    for i in range(M):
        i, j = map(int,input().split())
        arr[i][j] = 1
        arr[j][i] = 1

    # for row in arr:
    #     print(row)
    for i in range(1, N+1):
        result =[]
        dfs(i, result)
        result2.append(result)
    print(result2)
    count = 0
    for row in result2:
        if len(row) > 0 :
            count += 1

    print("#{} {}".format(tc, count))


