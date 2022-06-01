import sys
sys.stdin = open('input.txt','r')

def find(row,start,end):
    global cnt
    len = end - start +1
    half = len//2 if len % 2 == 0 else len//2+1
    # stack으로 문제풀기
    s = []
    for i in range(start, start+half):
        s.append(map[row][i])
    if len % 2 == 1:
        s.pop()
    if len != 1:
        for i in range(start+half, end+1):
            if s.pop() != map[row][i]:
                return
    # 회문 발견함
    if cnt < len:
        cnt = len

T = 10
N = 100
for tc in range(1, T+1):
    int(input())
    map = [list(input()) for _ in range(N)]
    # print(map)
    # 세로방향으로 배열 추가하기
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(map[j][i])
        map.append(temp)
    # for row in map:
    #     print(row)
    cnt = 0 # 회문의 길이
    for i in range(2*N):
        for j in range(N):
            for k in range(N):
                if k-j+1 > cnt:  # 현재까지 찾아낸 최장회문(cnt)보다 길어야 탐색 시작
                    find(i,j,k)
    print("#{} {}".format(tc,cnt))