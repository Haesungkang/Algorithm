import sys
sys.stdin = open('sample_input.txt', 'r')
sys.setrecursionlimit(1000000)

from collections import deque

def find(N, M, cnt):
    global minV, result
    q = deque()
    q.append(N)

    while q:

        for i in range(len(q)):
            A = q.popleft()

            if A <= 0 or A > 1000000: continue
            if A == M:
                return cnt

            if visited[A] == 0:
                visited[A] = 1
                q.append(A*2)
                q.append(A+1)
                q.append(A-10)
                q.append(A-1)

        cnt += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = False
    minV = 1000000
    visited = [0] * 1000001

    print("#{} {}".format(tc,find(N, M, 0)))
