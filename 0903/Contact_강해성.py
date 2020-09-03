import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    Q = []
    visit = [0] * (101)
    dis_idx = [0] * (101)

    #처음 start지정
    Q.append(v)
    visit[v] = 1
    dis_idx[v] = 0
    # Q에 있는동안 검색
    while Q:
        v = Q.pop(0)
        d = dis_idx[v]
        for w in range(1, 101):
            if B[v][w] == 1 and visit[w] == 0:
                Q.append(w)
                dis_idx[w] = d+1
                visit[w] = 1

    return dis_idx

for tc in range(1, 11):
    L, S = map(int, input().split())
    temp = list(map(int, input().split()))

    B = [[0] * (101) for _ in range(101)]

    for i in range(len(temp)//2):
        s, e = temp[2 * i], temp[2 * i + 1]
        B[s][e] = 1

    maxnumber = max(dfs(S))
    max_idx = []
    for i in range(len(dfs(S))):
        if dfs(S)[i] == maxnumber:
            max_idx.append(i)
    print("#{} {}".format(tc,max(max_idx)))