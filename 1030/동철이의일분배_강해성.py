import sys
sys.stdin = open('input.txt', 'r')


def perm(k, work):
    global maxpercent
    if work <= maxpercent:
        return
    if k == N:
        if work >= maxpercent:
            maxpercent = work
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            perm(k+1, work * arrlist[k][i] / 100)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arrlist =  [list(map(int, input().split())) for _ in range(N)]
    #print(arrlist)
    arr = [i for i in range(N) ]
    maxpercent = 0

    visited = [0] * N
    perm(0, 1)

    print("#{}".format(tc), end=" ")
    print("%0.6f" % (100 * maxpercent))