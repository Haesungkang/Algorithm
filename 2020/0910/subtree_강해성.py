import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(N):
    global cnt
    cnt += 1
    for i in tree[N]:
        dfs(i)

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    #print(arr)
    tree = [[] for _ in range(E+2)]
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        tree[p].append(c)
    cnt = 0
    # print(tree)
    dfs(N)

    print("#{} {}".format(tc, cnt))
