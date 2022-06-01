import sys
sys.stdin = open("sample_input_3.txt", "r")

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def boundary(nr, nc):
    if nr < 0 or nr >=N or nc < 0 or nc >= N:
        return True
    else:
        False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(n) for n in input()] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    #출발점 찾기
    result = 0
    nr = 0
    nc = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                nr = i
                nc = j

        stack = [(nr, nc)]
    #출발점에서부터 3(목표지점)으로 접근하기
    while len(stack) > 0:
        # stack의 값이 있을동안
        nr, nc = stack[-1]
        visited[nr][nc] = 1
        falsecount = 0
        # stack에서 추출하고난다음에
        for k in range(4):
            nr, nc = stack[-1]
            visited[nr][nc] = 1
            nr += dr[k]
            nc += dc[k]
            #바운더리안에 들어가있는지 확인
            if boundary(nr, nc):
                falsecount += 1
                continue
            #0일경우 stack쌓은다음에 추가하기
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                stack.append((nr,nc))
                break
            if arr[nr][nc] == 3 and visited[nr][nc] == 0:
                result += 1
                nr -= dr[k]
                nc -= dc[k]
                break
            else:
                falsecount += 1
            #print(stack)
        if falsecount == 4:
            stack.pop()
        if result == 1:
            break
    print("#{} {}".format(tc,result))






