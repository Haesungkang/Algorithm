import sys
sys.stdin = open("sample_input.txt", "r")

def search(depth, nr, nc, cur_string):
    #blank[nr][nc] = 1
    length = len(cur_string)
    # depth까지 도달할경우
    if length == depth:
        # result = ''
        # for i in range(4):
        #     for j in range(4):
        #         if blank[i][j] == 1:
        #             result = result + str(arr[i][j])
        result.add(cur_string)
        return
    else:
        #자신 선택하고 사방으로 방향을 만든다음에 다음으로 전달
        for k in range(4):
            nrr = nr + dr[k]
            ncc = nc + dc[k]
            if 0 <= nrr < 4 and 0 <= ncc < 4:
                search(depth, nrr, ncc, cur_string+str(arr[nrr][ncc]))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            nrr = i
            ncc = j
            search(7, nrr, ncc, str(arr[i][j]))

    print("#{} {}".format(tc, len(result)))


