import sys
sys.stdin = open("input.txt", "r")

'''

- 자성체만 고려함 ( 0이 아닐떄)

2일떄
- 내려오면서 방해물을 만났을떄(1을 만났을떄) => 교착
- 내려오면서 방해물을 못만났을때 -> 교착없음

1일떄
- 방해물임을 표시해준다

'''

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 #교착횟수 저장
    for c in range(N):  #열방향 순회
        obstacle = 0    #1 #방해물 저장
        for r in range(N):  #세로방향순회
            if arr[r][c] == 0: #2 #자성체가 없으면 건너띄기
                continue
            elif arr[r][c] == 2 and obstacle == 0:
                #3 #S극인데 이제까지 방해물인 N극을 못만났을때
                continue
            elif arr[r][c] == 2 and obstacle != 0:
                #4 #S극인데 이제까지 방해물인 N극을 만났을때 => 교착
                cnt += 1
                obstacle = 0 #5 112이런식으로 교착이되었을때 고려해야하니깐 -=1로 하지않고 0으로 초기화 시킨다
            elif arr[r][c] == 1: #내려오면서 방해물(N극, 1) 만나면
                obstacle +=1
    print("#{} {}".format(tc, cnt))





































