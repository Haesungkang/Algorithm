import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    # for row in arr:
    #     print(row)

    ans = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]: #if문의 조건 자리에 0이면 false, 0이 아니면 true
                x = i
                while x < N and arr[x][j] != 0: #영역을 벗어나지않고, 0이 아닐동안 반복
                    y = j
                    while y < N and arr[x][y] != 0:
                        arr[x][y] = 0
                        y += 1
                    x +=1
                ans.append((x-i,y-j))
    # print(ans)
    for i in range(len(ans)-1):
        idx = i
        for j in range(i+1, len(ans)):
            # 행렬의 크기
            a = ans[idx][0] * ans[idx][1]
            b = ans[j][0] * ans[j][1]
            # 행렬의 크기가 같으면 행으로 비교
            if a > b:
                idx = j
            elif a == b and ans[idx][0] > ans[j][0]:
                idx = j
        ans[i], ans[idx] = ans[idx], ans[i]
    # print(ans)
    print("#%d %d" %(tc, len(ans)), end="")
    for a,b in ans:
        print(" %d %d" %(a, b), end="")
    print()