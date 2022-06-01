import sys
sys.stdin = open('sample_input_2.txt', 'r')

def dfs(st, cnt):
    global result
    n = charge[st]
    if cnt >= result:
        return
    #종료조건
    if st + n >= N-1:
        if cnt < result:
            result = cnt
        return

    for i in range(1, n+1):
        if charge[i] >= charge[n]:
            dfs(st+i, cnt+1)

T = int(input())
for tc in range(1, T+1):
    inputlist = list(map(int,input().split()))
    N = inputlist[0]
    station = [i for i in range(N)]
    charge = inputlist[1:]
    #시작점 & 횟수
    result = 9999999
    dfs(0, 0)
    print("#{} {}".format(tc, result))