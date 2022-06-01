import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max = 0
    sumlist =[]
    for sero in range(N-M+1):
        for garo in range(N-M+1):
            sum = 0
            for i in range(M):
                for j in range(M):
                    sum += arr[i+garo][j+sero]
            sumlist.append(sum)
    for i in sumlist:
        if max < i:
            max = i
    print("#{} {}".format(tc, max))