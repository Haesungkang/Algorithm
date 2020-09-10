import sys
sys.stdin = open("sample_input_1.txt", "r")

for tc in range(1, int(input())+1):
    N,M,L = map(int, input().split()) # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    tree = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    # print(tree)

    for i in range(len(tree)-1, 1, -1):
        #print(i, end= " ")
        tree[i//2] += tree[i]
    # print()
    # print(tree)
    print("#{} {}".format(tc, tree[L]))

