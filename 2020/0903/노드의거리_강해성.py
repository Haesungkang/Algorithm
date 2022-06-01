import sys
sys.stdin = open("sample_input (1).txt", "r")

def dfs(v, G):
    Q = []
    visit = [0] * (V+1)
    dis_idx = [0] * (V+1)

    #처음 start지정
    Q.append(v)
    visit[v] = 1
    dis_idx[v] = 0
    # Q에 있는동안 검색
    while Q:
        v = Q.pop(0)
        d = dis_idx[v]
        for w in range(1, V+1):
            if B[v][w] == 1 and visit[w] == 0:
                if w == G:
                    Q.append(w)
                    dis_idx[w] = d + 1
                    visit[w] = 1
                else:
                    Q.append(w)
                    dis_idx[w] = d+1
                    visit[w] = 1

    return dis_idx[G]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    B = [[0] * (V+1) for _ in range(V+1)]

    for k in range(E):
        i, j = map(int, input().split())
        B[i][j] = 1
        B[j][i] = 1
    S, G = map(int,input().split())

    print("#{} {}".format(tc, dfs(S, G)))

