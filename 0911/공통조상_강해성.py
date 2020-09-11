import sys
sys.stdin = open("input.txt", "r")


def dfs(N, result):
    for i in range(len(tree)):
        for j in tree[i]:
            if j == N:
                result.append(i)
                dfs(i, result)
    return result

def dfs2(N):
    global cnt
    cnt += 1
    for i in tree[N]:
        dfs2(i)

T = int(input())

for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    #print(arr)
    tree = [[] for _ in range(V+2)]
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        tree[p].append(c)
    #print(tree)

    result1 = []
    result2 = []
    dfs(A, result1)
    dfs(B, result2)
    finalresult = 0
    for i in result1:
        if i in result2:
            finalresult = i
            break

    cnt = 0
    dfs2(finalresult)

    print("#{} {} {}".format(tc, finalresult, cnt))

