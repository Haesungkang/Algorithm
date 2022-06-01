import sys
sys.stdin = open('input.txt', 'r')

def find(k, percent):
    global maxV
    if k == N:  # 순열을 다고르면
        if maxV < percent: # 확률중 가장 좋은거 고르기
            maxV = percent
        return
    for i in range(N):
        if not visited[i] and p[k][i] != 0:
            visited[i] = True
            find(k+1, percent*p[k][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [ list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] /= 100

    sel = [0] * N
    visited = [False] * N
    maxV = 0
    find(0, 1)
    print("#{} {:.6f}".format(tc, maxV*100))