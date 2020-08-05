

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    blank = [[0 for _ in range(N)] for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    nr = 0
    nc = 0
    count = 1
    for i in range(0, 10):
        if count == (N**2)+1:
            break
        for k in range(4):
            if count == (N ** 2) + 1 :
                break
            while 0 <= nr < len(blank) and 0 <= nc < len(blank):

                if blank[nr][nc] != 0:
                    nr += dr[k]
                    nc += dc[k]
                    blank[nr][nc] = count

                blank[nr][nc] = count
                nr += dr[k]
                nc += dc[k]
                count += 1

                if nr >= len(blank):
                    nr -= 1
                    break
                if nc >= len(blank):
                    nc -= 1
                    break
                if nr < 0 :
                    nr +=1
                    break
                if nc < 0 :
                    nc +=1
                    break
                if blank[nr][nc] != 0:
                    if k == 3:
                        nr +=1
                    if k == 0:
                        nc -=1
                    if k == 1:
                        nr -=1
                    if k == 2:
                        nc +=1
                    break

    print("#{}".format(tc))
    for i in range(len(blank)):
        for j in range(len(blank[i])):
            print(blank[i][j], end=' ')
        print()
