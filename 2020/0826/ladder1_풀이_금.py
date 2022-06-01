import sys
sys.stdin = open("input.txt","r")

def check(x, y):
    if x < 0 or x >= 100 or y < 0 or y >= 100: return False
    if arr[x][y] == 0: return False
    return True

for tc in range(1,11):
    case_num = input()
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 도착점을 찾는다.

    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break
    dir = 0 #방향정보 저장 0: 위, 1:좌, 2:우

    # while x:
    #     #왼쪽으로 가는 경우
    #     if dir != 2 and check(x, y-1):
    #         y -= 1; dir = 1
    #     #오른쪽으로 가는경우
    #     elif dir != 1 and check(x, y+1):
    #         y += 1; dir = 2
    #     # 그외, 위로 가는경우
    #     else:
    #         x -= 1; dir = 0
    #
    # print(y)


    # 길을 지우면서 조작하는 경우
    # while x:
    #     arr[x][y] = 0
    #     #왼쪽으로 가는 경우
    #     if check(x, y-1):
    #         y -= 1
    #     #오른쪽으로 가는경우
    #     elif check(x, y+1):
    #         y += 1
    #     # 그외, 위로 가는경우
    #     else:
    #         x -= 1
    def ladder(x, y):
        if x == 0:
            # global ans; ans= y
            return y
        else:
            while x:
                arr[x][y] = 0
                #왼쪽으로 가는 경우
                if check(x, y-1):
                    return ladder(x, y-1)  # ladder2를 적용할경우 +1을이용해서 count 한다
                #오른쪽으로 가는경우
                elif check(x, y+1):
                    return ladder(x, y +1)
                # 그외, 위로 가는경우
                else:
                    return ladder(x -1 , y)
                #arr[x][y] =1,2 다시 1로 채운다 원상복구시킨다

    print(ladder(x, y))