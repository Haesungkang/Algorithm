import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    # for row in puzzle:
    #     print(row)
    # 횟수 for
    # 조건들이 포함되어있을땐 while
    dist = 0 # 자릿수

    for i in range(N):  #가로방향검사
        words = 0 # 빈칸수
        cur = 0 # 현재위치
        while cur < N:
            if puzzle[i][cur] == 1: #1일때 카운팅시작
                words += 1 #한칸씩 세어나감
                if words == K and cur == N-1: #K길이의 칸을 찾고 마지막까지 찾았으면
                    dist +=1
            else: # 0일때 [1,1,1,0,1] [1,1,1,1,0]구분
                if words == K: # 이제까지 세어온 빈칸수가 K면
                    dist += 1
                words = 0 #[1,1,1,0,1]에서 다시 리셋을 해야하니깐
            cur += 1

    for i in range(N):  #세로방향검사
        words = 0 # 빈칸수
        cur = 0 # 현재위치
        while cur < N:
            if puzzle[cur][i] == 1: #1일때 카운팅시작
                words += 1 #한칸씩 세어나감
                if words == K and cur == N-1: #K길이의 칸을 찾고 마지막까지 찾았으면
                    dist +=1
            else: # 0일때 [1,1,1,0,1] [1,1,1,1,0]구분
                if words == K: # 이제까지 세어온 빈칸수가 K면
                    dist += 1
                words = 0
            cur += 1

    print("#{} {}".format(tc,dist))

