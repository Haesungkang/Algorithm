import sys
sys.stdin = open('sample_input_2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for i in range(E):
        n1, n2, c = map(int, input().split())
        adj[n1].append([n2,c])

    INF = 999999
    dist = [INF] * (V+1)
    selected = [False] * (V+1)
    dist[0] = 0
    cnt = 0
    while cnt <= V:
        minV = INF
        u = -1
        for i in range(V+1):
            if not selected[i] and minV > dist[i]:
                minV = dist[i]
                u = i
        selected[u] = True
        cnt += 1
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print("#{} {}".format(tc, dist[-1]))
