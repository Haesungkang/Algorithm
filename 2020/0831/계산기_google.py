import sys
sys.stdin = open('input.txt', 'r')

# 연산자의 순위 표시 (숫자가 낮을수록 우선순위가 높음)
def rank(operator):
    if operator == '*' or operator == '/':
        return 0
    elif operator == '+' or operator == '-':
        return 1
    elif operator == '(' or operator == ')':
        return 2
    else:
        return 3

# 중위 표기(매개변수)를 후위 표기로 바꾸는 함수
def postfix_notation(calculation_list):
    stack = []  # 연산자 임시 저장
    result = []  # 후위연산으로 바꾼 결과 저장
    for i in calculation_list:

        # 숫자
        if type(i) is int:
            # 그대로 출력
            result.append(i)

        # 연산자
        else:

            # 여는 괄호는 무조건 stack에 추가
            if i == '(':
                stack.append(i)

            elif i == ')':

                # 닫는 괄호가 나오면 여는 괄호가 나올 때까지 stack을 모두 pop
                # 괄호 사이에 있는 연산들은 모두 괄호 안에서 처리되어야 하기 때문이다.
                # stack은 연산 우선순위 역순으로 정리되어 있기 때문에 pop()을 하면 연산 우선순위대로 나온다.
                for k in stack:

                    # 여는 괄호가 나오면 순회 종료
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        result.append(stack.pop())
            else:
                # 스택이 비었으면 stack 추가
                if not stack:
                    stack.append(i)

                # 스택에 들어있는 연산자와 순위 비교
                else:

                    # 현재 연산자(i)가 stack에 들어있는 연산자보다 우선순위가 높으면, stack에 추가
                    if rank(i) < rank(stack[-1]):
                        stack.append(i)

                    # 우선순위가 같거나 낮으면, stack에 있는 연산자를 pop하고, 현재 연산자를 stack에 추가
                    else:
                        result.append(stack.pop())
                        stack.append(i)

    # stack에 남은 연산자 모두 출력
    for j in stack:
        result.append(stack.pop())
    # print(stack)
    return result

for tc in range(1, 4):
    L = int(input())
    text = input()
    # 초기값 input list로 만들어주기
    infix = []
    for idx in range(L):
        infix.append(text[idx])
    print(infix)
    print(postfix_notation(infix))
    print()