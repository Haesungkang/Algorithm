import sys

sys.stdin = open('./inputfolder/input2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    count = 2 * D + 1
    if N%count== 0:
        answer = N//count
    else:
        answer = N//count + 1
    #print(N, D)
    print("#{} {}".format(tc, answer))

