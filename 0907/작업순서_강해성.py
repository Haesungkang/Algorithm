import sys
sys.stdin = open("input_1.txt", "r")

def dfs(v, result):

    if visited[v] == 1:
        pass
    else:
        visited[v] = 1
        result.append(v)

        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                falsecount = 0
                for i in range(V+1):
                    if G[i][w] == 1 and visited[i] == 0:
                        falsecount += 1
                if falsecount == 0:
                    dfs(w, result)


for tc in range(1, 11):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    visited = [0] * (V + 1)

    for i in range(E):
        s, e = temp[2 * i], temp[2 * i + 1]
        G[s][e] = 1

    # for row in G:
    #     print(row)

    # 처음에 아무것도 필요가 없는 친구 하나를 선정해서 dfs작업을 한다
    # 그다음 dfs를 할때 그전에 해야되는 task가 있으면은 안된다
    # 이런식으로 계속 앞에 있는 task없는거를 계속 dfs작업을 해야한다
    startlist = []
    for j in range(1, V+1):
        count = 0
        for i in range(1, V+1):
            if G[i][j] == 0:
                count += 1
        if count == V:
            startlist.append(j)
    #print(startlist)

    result = []
    for i in range(len(startlist)):
        route = []
        dfs(startlist[i], route)
        result.append(route)

    print("#{}".format(tc), end=" ")
    for row in result:
        for i in row:
            print(i, end=" ")
    print()


