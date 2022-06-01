import sys
sys.stdin = open("sample_input_1.txt", "r")

T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[i for i in input()] for _ in range(N)]
    ans = 0

    # 맨위맨아래 칠하기
    for i in range(M):
        if arr[0][i] != 'W':
            ans += 1
            arr[0][i] = "W"
    for i in range(M):
        if arr[N-1][i] != 'R':
            ans += 1
            arr[N - 1][i] = 'R'

    for row in arr:
        print(row)

    #print(ans)
    #각자 카운트시키기
    Wc = []
    Bc = []
    Rc = []
    for i in range(N):
        count1 = 0
        count2 = 0
        count3 = 0
        for j in range(M):
            if arr[i][j] == "W":
                count1 +=1
            if arr[i][j] == "B":
                count2 +=1
            if arr[i][j] == "R":
                count3 +=1
        Wc.append(count1)
        Bc.append(count2)
        Rc.append(count3)
    print(Wc)
    print(Bc)
    print(Rc)

    blist = []
    rlist = []
    wlist = []
    # 파랑색 기준으로
    for i in range(1, N-1):
        blist.append(Wc[i] - Bc[i] + Rc[i])
        rlist.append(Bc[i] - Rc[i] + Wc[i])
        wlist.append(Bc[i] - Wc[i] + Rc[i])

    print(wlist)
    print(blist)
    print(rlist)
    # finallist = []
    # for i in range(len(wblist)):
    #     a= sum(wblist[:i+1])
    #     b= sum(brlist[i+1:len(wblist)])
    #     finallist.append(a+b)
    # print(finallist)
    # print(ans + min(finallist))




    # counting = []
    # for i in range(1, N-1):
    #     k = i
    #     bluecount = 0
    #     while 0 < k:
    #         bluecount += Wc[k]
    #         bluecount += Rc[k]
    #         k -= 1
    #     k = i
    #     redcount = 0
    #     while k < N-1:
    #         k += 1
    #         redcount += Wc[k]
    #         redcount += Bc[k]
    #     counting.append(bluecount+redcount)
    #
    # print(counting)





    # #파랑색 한줄 칠할때마다 그 위아래 비교
    # for i in range(1, N-1):
    #     #일단 파란색 한줄은 칠했고
    #     box = 0
    #     for j in range(M):
    #         if arr[i][j] != "B":
    #             box += 1
    #     # 나머지 순차로 진행하면서 WB + BR min값 찾기
    #     box += compare(1, i, "W", "B")
    #     # i번째 파란색으로 칠해지면
    #     box += compare(i+1, N-1, "B", "R")
    #     print(box)



    # def compare(S, E, color_1, color_2):
    #     ans = 0
    #
    #     for i in range(S, E+1):
    #         color1 = 0
    #         color2 = 0
    #         for j in range(M):
    #             if arr[i][j] == color_1:
    #                 color1 += 1
    #             if arr[i][j] == color_2:
    #                 color2 += 1
    #         #해당줄에서 두번째 색상이 더 많다면
    #         if color1 < color2:
    #

    # return ans


