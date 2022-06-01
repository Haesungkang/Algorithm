import sys
sys.stdin = open('input_1.txt', 'r')

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def perm(customer, idx, path, visited):
    global minV
    if idx == N:
        # 거리계산
        # 회사 = 첫번쨰 방문 고객 -> 순열대로 방문
        # 마지막 고객 - 집으로 고고띵
        dist = 0
        dist += abs(company.x - path[0].x) + abs(company.y - path[0].y)
        for i in range(N-1):
            dist += abs(path[i].x - path[i+1].x) + abs(path[i].y - path[i+1].y)
        dist += abs(path[N-1].x - home.x) + abs(path[N-1].y - home.y)
        if minV > dist:
            minV = dist
        return
    # 아니면 순열 계속만들어나감
    for i in range(N):
        if visited[i] == 0:
            path[idx] = customer[i]
            visited[i] = 1
            perm(customer, idx+1, path, visited)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = Point(arr[0],arr[1])
    home = Point(arr[2],arr[3])
    customer = []
    for i in range(2, N+2):
        customer.append(Point(arr[2*i],arr[2*i+1]))
    visited = [0] * N
    minV = 100000
    path = [0] * N
    perm(customer, 0, path, visited)
    print("#{} {}".format(tc, minV))