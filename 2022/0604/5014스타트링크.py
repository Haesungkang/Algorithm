import sys
from collections import deque
sys.stdin = open('./2022/inputfolder/5014.txt', 'r')

f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)
queue = deque()
check = False
def bfs(s):
    global check
    queue.append(s)
    while queue:
        x = queue.popleft()
        if x == g:
            check = True
            return 
        for i in (x-d, x+u):
            if i < 0 or i > f or i == s:
                continue
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)

bfs(s)

if check == True or visited[g] > 0:
    print(visited[g])
else:
    print("use the stairs")

