import sys
sys.stdin = open('sample_input_3.txt', 'r')

def find():
    for i in range(N):
        for j in range(N-M+1):
            k = 0
            h = M//2
            while k < h:
                if s[i][j+k] != s[i][j+M-1-k]:
                    break
                k+=1
            if k == h:
                print(s[i][j:j+M])
                return
            k = 0
            while k < h:
                if s[j+k][i] != s[j+M-1-k][i]:
                    break
                k +=1
            if k == h:
                for l in range(j, j+M):
                    print(s[l][i], end='')
                print()
                return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    s = [input() for _ in range(N)]
    # print(s)
    print("#{}".format(tc), end=" ")
    find()