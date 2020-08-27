import sys
sys.stdin = open("input.txt","r")

def search(r,c):
    count = 0
    dr = [0,0,1]
    dc = [-1,1,0]
    num = ladder[r][c]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[r][c] = 1

    while True:
        if r == 99:
            return count

        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc<0 or nc >= N: continue
            if ladder[nr][nc] == 0: continue
            if visited[nr][nc] == 1: continue
            r = nr
            c = nc
            num = ladder[nr][nc]
            visited[nr][nc] = 1
            count += 1
            break

T = 10
for tc in range(1, T+1):
    N = 100
    int(input())
    ladder = [list(map(int,input().split())) for _ in range(N)]
    count_list = []
    x_idx = []
    for i in range(N):
        if ladder[0][i] == 1:
            result = search(0, i)
            count_list.append(result)
            x_idx.append(i)
    min = 1000
    min_idx = 0
    print(count_list)
    print(x_idx)
    for i in range(len(count_list)):
        if min >= count_list[i]:
            if min == count_list[i]:
                if x_idx[i] > x_idx[min_idx]:
                    min = count_list[i]
                    min_idx = i
            min = count_list[i]
            min_idx = i
    print("#{} {}".format(tc, x_idx[min_idx]))



