import sys
sys.stdin = open("sample_input.txt", "r")

def search(x):
    if x == "*" or x == "+" or x == "-" or x == "/":
        return 1
    else:
        return 2

def cal(a, b, i):
    if i == "*":
        number = a * b
        return  number
    elif i == "/":
        number = a // b
        return  number
    elif i == "+":
        number = a + b
        return  number
    elif i == "-":
        number = a - b
        return  number

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    # 오류횟수 저장
    falsecount = 0
    # 맨끝에 .이 없을경우
    if arr[-1] != '.':
        falsecount += 1
    for i in arr:
        # 연산이 아닐경우(정수일 경우) 추가
        if search(i) == 2:
            stack.append(i)
        else:
            # 연산일경우 스택에서 숫자가 2개있어야함
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                # 뽑아낸것이 모두 숫자이여야만함
                if a != "." and b != ".":
                    int_a = int(a)
                    int_b = int(b)
                    stack.append(cal(int_a,int_b,i))
                else:
                    falsecount += 1
            # 숫자가 2개 없을경우
            else:
                falsecount += 1
    # print(stack)
    # stack에서 .이 마지막에 나와서 stack만되고 ex) [10, .] 형태로 남았을떄 출력하기
    if len(stack) == 2 and falsecount == 0:
        #[..]2개일경우 예외처리
        if stack[0] != ".":
            print("#{} {}".format(tc,stack[0]))
        else:
            print('#{} error'.format(tc))
    else:
        print('#{} error'.format(tc))
