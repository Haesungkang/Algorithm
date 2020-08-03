import sys
sys.stdin = open('../0inputlist/input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    #입력
    N, M = map(int, input().split())
    # range에서 0,1,2,3, (_는 변수가 필요없을경우)
    room = [[0 for _ in range(M)] for _ in range(N)]
    print(room)
    boxTop = list(map(int, input().split()))
    # gravity 그림에 나온거 처럼 1에다가 넣기
    for i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1

    max = 0 # 최대낙차 저장하기위한 변수

    for i in range(N):
        if boxTop[i] > 0: # 상자가 있다면
            dist = 0
            for j in range(i+1, N): #상자위치 한칸 다음부터 마지막까지 반복
                if room[j][boxTop[i]-1] == 0: # boxTop고정 index로 확인중
                    dist += 1 # 개수 카운팅
            if max < dist:
                max = dist
    print(max)








    # for row in room:
    #     print(row)
    #계산

    #출력