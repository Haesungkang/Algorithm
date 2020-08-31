import sys
sys.stdin = open('input.txt', 'r')

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
                    postfix.append(x)
                # for j in stack:
                #     if stack[-1] == "(":
                #         stack.pop()
                #         break
                #     # 괄호안에 있는 연산자 생각해서 postfix에 추가
                #     else:
                #         postfix.append(stack.pop())
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
    # 남은 요소 천부 postfix에 추가
    print(postfix)
    # print(stack)
    # for t in range(len(stack)-1, -1, -1):
    #     if pre(stack[t]) == 4 or pre(stack[t]) == 3:
    #         postfix.append(stack[t])
    for j in stack:
        postfix.append(stack.pop())



    # print(postfix)
    # print()
    stack = []
    for i in postfix:
        if pre(i) == 1:
            stack.append(i)

        else:
            b = int(stack.pop())
            a = int(stack.pop())

            if i == '+':
                cal = a+b
            if i == '*':
                cal = a*b

            stack.append(cal)

    # print(stack[0])
    print("#{} {}".format(tc, stack[0]))






# for tc in range(1, int(input()) + 1):
#     arr = input()
#     S = []
#
#     # 한문자씩 읽어서 처리
#     ans = 1
#     for ch in arr:
#         if ch == '(' or ch == '{':
#             S.append(ch)
#         if ch == ')' or ch == '}':
#             # 빈스택일경우
#             if len(S) == 0:
#                 ans = 0;
#                 break
#             t = S.pop()
#             if (ch == ')' and t != '(') or (ch == '}' and t != '{'):
#                 ans = 0;
#                 break
#         # else: #안해도된다
#     if len(S) != 0:  # 빈스택인지조사
#         ans = 0
#     print(ans)


