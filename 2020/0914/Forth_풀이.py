import sys
sys.stdin = open("sample_input.txt", "r")

def find():
    #읽기만하기때문에 굳이 가져올필요가없다 그래서 매개변수 없는걸로 시작
    s = [] #스택준비
    for i in range(len(code)):
        #연산자면 연산하기
        if code[i] == "+" or code[i] == "-" or code[i] == "*" or code[i] == "/":
            #연산
            if len(s) >= 2: # 연산하려고 할떄 스택에 2개이상 들어있어야함
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == "+":
                    s.append(op1 + op2)
                elif code[i] == "-":
                    s.append(op1 - op2)
                elif code[i] == "*":
                    s.append(op1 * op2)
                elif code[i] == "/":
                    s.append(op1 // op2)
            else:
                return "error"


        # 아니면은 숫자면은 스택에 넣기
        elif code[i] != ' ' and code[i] != '.':
            s.append(code[i])
        elif code[i] == ".":
            if len(s) == 1:
                return s.pop()
            else:
                return "error"


T = int(input())
for tc in range(1, T+1):
    #문자열 숫자가 섞여있을땐, 문자로 전부받은후에 숫자는 숫자로 바꾸는게 좋다
    code = list(input().split())
    #print(code)
    print("#{} {}".format(tc, find()))