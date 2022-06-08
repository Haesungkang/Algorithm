import sys
sys.stdin = open('./2022/inputfolder/2644.txt', 'r')

n = int(input())
a, b = map(int,input().split())
node = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(node):
    i , j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1

visited = [0] * (n+1)
result = []

# cnt를 따로 저장하는 과정
# 차라리 처음에 cnt를 추가해라 
def dfs(x, cnt):
    cnt += 1
    visited[x] = 1
    #비슷한 생각을 했는데, 여기서 result로 추가해라
    if x == b:
        result.append(cnt)

    for w in range(n+1):
        if arr[x][w] == 1 and visited[w] == 0:
            dfs(w, cnt)

dfs(a, 0)
#print(result)
if len(result) == 0:
    print(-1)
else: 
    print(result[0]-1)



