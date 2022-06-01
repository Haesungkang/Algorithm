import sys
sys.stdin = open("input.txt", "r")

def inorder(n): #n : 현재 정점
    if n <= N:
        inorder(n*2)    #왼쪽 자식 순회
        print(tree[n], end="")
        inorder(n*2+1)  #오른쪽 자식 순회



T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)  #1차원 배열로 트리 구현 ( 완전 이진트리 )
    for i in range(N):
        node = list(input().split())  #한줄읽기
        tree[int(node[0])] = node[1]
        #print(node)
    print(tree)
    #중위순회하기
    print("#{}".format(tc), end=" ")
    inorder(1)
    print()