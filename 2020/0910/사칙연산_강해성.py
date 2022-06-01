import sys
sys.stdin = open("input.txt", "r")

operator = ['+','*','-','/']

def postorder(idx):     #왼,오른쪽,부모 =>  LRV
    global postfix
    if idx <= lastidx:
        #왼쪽
        postorder(2*idx)     #왼쪽자식
        #오른쪽
        postorder(2*idx + 1)     #오른쪽자식
        #현재노드 방문 (출력)
        postfix.append(tree[idx])

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    postfix = []
    for i in range(N):
        node = list(input().split())  #한줄읽기
        tree[int(node[0])] = node[1]
    print(tree)
    lastidx = N
    postorder(1)
    print(postfix)
    stack = []
    for c in postfix:
        if c not in operator: # 숫자면
            stack.append(int(c))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if c == "+":
                stack.append(op2 + op1)
            if c == "*":
                stack.append(op2 * op1)
            if c == "/":
                stack.append(op2 / op1)
            if c == "-":
                stack.append(op2 - op1)
    result = stack.pop()
    print("#{} {}".format(tc, int(result)))
