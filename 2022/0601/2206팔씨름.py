import sys
sys.stdin = open('2022/0601/inputfolder/input4.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    # print(arr)
    N = len(arr)
    answer = "YES"
    winner = True
    win = 0
    lose = 0
    # print(N)
    for i in range(N):
        if arr[i] == "o":
            win += 1
        else:
            lose += 1
        if lose >= 8:
            winner = False
            break
        if win >= 8:
            winner = True
            break
    if winner:
        answer = "YES"
    else:
        answer = "NO"
    print("#{} {}".format(tc, answer))
    # 배우면 좋을것
    #         num = 0
    # for i in test:
    #     if i == "x":
    #         num += 1

    # 한번에 프린트해버리기
    # if num >= 8:
    #     print("#{} NO".format(test_case))
    # else:
    #     print("#{} YES".format(test_case))

    # if 15 - len(game) + game.count('o') > 7:
    #     print(f'#{test_case} YES')
    #     pass
    # else:
    #     print(f'#{test_case} NO')
    #     pass