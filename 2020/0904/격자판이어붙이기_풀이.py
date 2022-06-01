import sys
sys.stdin = open("sample_input.txt", "r")
#완전탐색 -> 깊이우선탐색
# 모든좌표에서 모든 경우의 수를 탐색(dfs탐색)
# 중복없이 자료 저장(set)

dr = [-1, 0, 0, 1]
dc = [0, 1, -1, 0]

def dfs(r, c, cnt, num): # r,c : 좌표, #cnt : 숫자의 개수, num : 숫자
    if cnt == 7:
        #만들어진 숫자 셋어 넣고 끝
        return
    for k in range(4):
        nr = r + dr[k]  #새좌표 계산
        nc = c + dc[k]
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4: continue
        dfs(nr,nc, cnt+1, num*10 + mat[nr][nc])


T = int(input())
for tc in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, 0)
    print("#{} ")