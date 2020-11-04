import sys
sys.stdin = open('sample_input.txt', 'r')

def graph(v, l):
    global cnt, q
    visited[v] = 1

    while q:

        if l == 2:
            return

        for _ in range(len(q)):

            friend = q.pop(0)
            visited[friend] = 1

            for w in range(N+1):
                if G[friend][w] == 1 and visited[w] == 0:
                    print(w)
                    #if w not in q:
                    q.append(w)
                    cnt += 1
        print(q)
        l += 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    q = []
    for i in range(M):
        a, b = map(int, input().split())
        G[a][b] = 1
        G[b][a] = 1
    # for row in G:
    #     print(row)
    q.append(1)
    graph(1, 0)
    print("#{} {}".format(tc, cnt))