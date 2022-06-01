import sys
sys.stdin = open("input.txt","r")

def search(r, c):
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    visited[r][c] = 1
    cnt = 0
    while True:
        if r == 99:
            return cnt
        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= 100 or nc < 0 or nc >= 100:
                continue
            if ladder[nr][nc] == 0:
                continue
            if visited[nr][nc] == 1:
                continue
            r = nr
            c = nc
            visited[nr][nc] = 1
            cnt += 1
            break


for test_case in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_index = 0
    min = 100
    for i in range(100):
        if ladder[0][i] == 1:
            result = search(0, i)
            print(result)
        if result:
            # print(result)
            if min >= result:
                min_index = i
                min = result
    print(f"#{tc} {i}")