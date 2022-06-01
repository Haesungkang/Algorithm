import sys
sys.stdin = open("sample_input_2.txt", "r")

#중위순회
def inorder(idx):     #왼,부모,오른쪽 =>  LVR
    if idx <= lastidx:
        #왼쪽
        inorder(2*idx)     #왼쪽자식
        #현재노드 방문 (출력)
        print(tree[idx] ,end=" ")
        #오른쪽
        inorder(2*idx + 1)     #오른쪽자식

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    number = [i for i in range(N+1)]
    visited = [0] * (N+1)
    #print(tree)
    start_i = 0
    for i in range(11):
        if (2 ** i) <= N:
            start_i = i
    start = (2 ** (start_i))

    cnt = 1
    #처음숫자 넣기
    tree[start] = cnt
    visited[start] = 1
    # 숫자 더하기
    #나누기 2
    while start > 1:
        cnt += 1
        start = start//2
        tree[start] = cnt
        visited[start] = 1
        #곱하기 2 +1 존재시
        if (start*2 + 1) <= N and visited[start*2 + 1] == 0 and start != 1:
            cnt += 1
            tree[start*2 + 1] = cnt
            visited[start*2 + 1] = 1

    for i in range(1, 10):
        if 3 * (2 ** i) <= N:
            start = 3 * (2 ** i)

    print(start)
    cnt += 1
    tree[start] = cnt
    visited[start] = 1

    while start > 3:
        cnt += 1
        start = start//2
        tree[start] = cnt
        visited[start] = 1
        #곱하기 2 +1 존재시
        if (start*2 + 1) <= N and visited[start*2 + 1] == 0 and start != 1:
            cnt += 1
            tree[start*2 + 1] = cnt
            visited[start*2 + 1] = 1

    print(number)
    print(tree)
    #print(tree[1], tree[N//2])
    


