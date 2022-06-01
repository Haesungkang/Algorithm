import sys
sys.stdin = open('input.txt', 'r')

# 우선순위 설정 (연산자, 괄호, 숫자순으로)
def pre(x):
    if x == "*":
        return 4
    if x == "+":
        return 3
    if x == "(" or x == ")":
        return 2
    else:
        return 1


for tc in range(1, 11):
    L = int(input())
    text = input()
    # 초기값 input list로 만들어주기
    infix = []
    for idx in range(L):
        infix.append(text[idx])
    # postfix, stack reset
    postfix = []
    stack = []
    # print(infix)

    for i in infix:
        # 숫자일 경우 바로 postfix 추가
        if pre(i) == 1:
            postfix.append(i)
        else:
            # 여는 괄호일경우 그냥 추가
            if i == '(':
                stack.append(i)
            # 닫는 괄호일경우 여는괄호 나올때 까지 pop
            elif i == ')':
                while True:
                    x = stack.pop()
                    if x == "(":
                        break
                    # 괄호안에 있는 값들은 다시 넣어줘야한다
                    postfix.append(x)

            else:
                #stack에 아무것도 없을때 추가하기
                if not stack:
                    stack.append(i)
                # 우선순위 연산자에 따라서 stack에 추가하기
                else:
                    if pre(i) > pre(stack[-1]):
                        stack.append(i)

                    else:
                        postfix.append(stack.pop())
                        stack.append(i)

    for i in postfix:
        print(i, end=' ')
    #다시 빈 stack만들기
    stack = []
    for i in postfix:
        # 숫자일 경우 stack에 추가
        if pre(i) == 1:
            stack.append(i)
        # 연산이 나왔을경우, 2개의 숫자를 뽑아내서 계산
        else:
            b = int(stack.pop())
            a = int(stack.pop())

            if i == '+':
                cal = a+b
            if i == '*':
                cal = a*b
            # 원래 stack 마지막에 추가
            stack.append(cal)
    print()
    # print("#{} {}".format(tc, stack[0]))



