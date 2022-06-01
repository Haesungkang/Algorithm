import sys
sys.stdin = open("sample_input (1).txt", "r")

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    G = [[0]* (V+1) for _ in range(V+1)]
    # G = [[]* (V+1) for _ in range(V+1)] 인접리스트

    for _ in range(E):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1
        # G[u].append(v)
        # G[v].append(u)

    s, e = map(int, input().split())    #출발, 도착

    visit = [0] * (V+1)
    Q = [s]
    visit[s] = 1    #출발점 방문하고 큐에 삽입

    while Q:            #빈큐가 아닐동안
        v = Q.pop(0)    #큐에 뺸다
                        #v의 방문하지 않은 인접 정점을 찾는다

        # if v == e: break

        for w in range(1, V+1):
        #for w in G[v]:
            if G[v][w] and not visit[w]:
                #if visit[w] == 0:
                visit[w] = visit[v] +1 #거리계산
                #if w == e: Q.clear(); break # 함수로 했을경우는 return
                Q.append(w)

    print( visit[e] -1 )
