import sys
sys.stdin = open('sample_input_1.txt', 'r')

def grouping(i):
    global cnt
    q = []
    visited[i] = 1
    q.append(i)
    #print(visited)
    while q:
        i = q.pop(0)
        for j in range(N+1):
            if G[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                q.append(j)
        #print(q)
    cnt += 1
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0

    for i in range(M):
        a, b = arr[2*i], arr[2*i+1]
        G[a][b] = 1
        G[b][a] = 1

    for i in range(1, N+1):
        if visited[i] == 0:
            grouping(i)


    print("#{} {}".format(tc, cnt))
