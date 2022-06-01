import sys
sys.stdin = open("input3.txt", "r")

bingo = [list(map(int, input().split())) for _ in range(5)]
blank = [[0 for _ in range(5)] for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

def check(blank):
    cnt = 0
    #가로세로 빙고확인
    for i in range(5):
        if sum(blank[i]) == 5:
            cnt += 1
        if (blank[0][i]+blank[1][i]+blank[2][i]+blank[3][i]+blank[4][i]) == 5:
            cnt += 1
    #대각선 빙고확인
    D = 0
    for i in range(5):
        D += blank[i][i]
    if D == 5:
        cnt +=1
    D1 = 0
    for i in range(5):
        D1 += blank[i][4-i]
    if D1 == 5:
        cnt += 1
    #빙고의 개수가 3이상일경우
    if cnt >= 3:
        return True
    else:
        return False

count = 0
breaking = False
for i in range(5):
    for j in range(5):
        count += 1
        #빙고와 부른숫자를 비교해서 blank에 삽입
        for a in range(5):
            for b in range(5):
                if call[i][j] == bingo[a][b]:
                    blank[a][b] = 1
                    if count > 10:
                        #만약 빙고가 됐으면 for문 빠져나오기
                        if check(blank):
                            print(count)
                            breaking = True
                            break
            if breaking:
                break
        if breaking:
            break
    if breaking:
        break


