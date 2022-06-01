import sys
sys.stdin = open('input.txt', 'r')

T = 10

operator = ['+','*']
braket = ["(",")"]

def isNumber(x):     #숫자인지 아닌지 판단
    if x not in operator and x not in braket:
        return True
    else:
        return False

def isp(token): #토큰의 우선순위 리턴 => 스택안의 토큰의 우선순위
    if token == "*" or token == "/":
        return 2
    elif token == "+" or token == "-":
        return 1
    elif token == "(":
        return 0

def icp(token): #스택 안으로 들어오는 토큰의 우선순위
    if token == "*" or token == "/":
        return 2
    elif token == "+" or token == "-":
        return 1
    elif token == "(":
        return 3


for tc in range(1, T+1):
    N = int(input())
    infix = list(input())
    #print(infix)
    postfix = []
    stack = []
    for c in infix:
        if isNumber(c):     #숫자일경우
            postfix.append(c)
        elif c == ")":      #닫는 괄호면 -> 여는괄호 만날때까지 팝
            while len(stack) > 0: #스택이 비어있지 않는 동안
                top = stack.pop()
                if top == "(": #여는 괄호 만나면 끝 (스택에 넣지도 않음)
                    break
                postfix.append(top)

        else:   #나머지연산자면(닫는 괄호가 아닌 연산자)
            if len(stack) == 0:     #스택이 비어있으면 스택에 그냥 넣기
                stack.append(c)
            else:   #아니면 우선순위 비교
                while len(stack) > 0:  #스택이 빌떄 까지 반복
                    top = stack[-1]     #스택의 가장 위의 원소
                    if icp(c) > isp(top): # 토큰의 우선순위가 스택의 top의 우선순위 보다 크면
                        stack.append(c)   # 스택에 넣음
                        break
                    postfix.append(stack.pop())
    #while len(stack) != 0:
    while stack:
        postfix.append(stack.pop())
    #print(postfix)
    # 후위 표기법을 계산 (stack을 이용하기)
    stack = []
    for c in postfix:
        if c not in operator: # 숫자면
            stack.append(int(c))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if c == "+":
                stack.append(op2 + op1)
            elif c == "*":
                stack.append(op2 * op1)
    result = stack.pop()
    print("#{} {}".format(tc, result))










