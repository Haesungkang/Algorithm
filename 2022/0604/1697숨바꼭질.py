import sys
from collections import deque
sys.stdin = open('./2022/inputfolder/1697.txt', 'r')


n, k = map(int, input().split())

queue = deque()
visited = [0] * 100001
def bfs(n):
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[k]
        for i in (x-1, x+1, 2*x):
            if 0<= i <100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)

print(bfs(n))


       

