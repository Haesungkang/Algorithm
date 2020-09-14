import sys
sys.stdin = open("sample_input.txt", "r")

def pre(x):
    if x == "*" or x == "/" or x == "+" or x == "-":
        return 3
    elif x == ".":
        return 2
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    postfix = list(input().split())
    stack = []
    falsecount = 0
    # print(postfix)
    for i in range(len(postfix)):
        # print(type(i.replace("'","")))
        print(postfix[i], end=" ")
        if pre(postfix[i]) == 1:
            stack.append(i)
        else:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                cal = int(a) postfix[i] int(b)
                stack.append(cal)
            # if postfix[i] == '+' and len(stack) > 1:
            #     b = stack.pop()
            #     a = stack.pop()
            #     cal = int(a) + int(b)
            #     stack.append(cal)
            # elif postfix[i] == '*' and len(stack) > 1:
            #     b = stack.pop()
            #     a = stack.pop()
            #     cal = int(a) * int(b)
            #     stack.append(cal)
            # elif postfix[i] == '-' and len(stack) > 1:
            #     b = stack.pop()
            #     a = stack.pop()
            #     cal = int(a) - int(b)
            #     stack.append(cal)
            # elif postfix[i] == '/' and len(stack) > 1:
            #     b = stack.pop()
            #     a = stack.pop()
            #     cal = int(a) / int(b)
            #     stack.append(cal)
            # else:
            #     falsecount += 1
    print(stack)
    print(falsecount)
    if falsecount == 1 and len(stack) == 1:
        if type(stack[0]) == int:
            print("#{} {}".format(tc, stack[0]))
        else:
            print("#{} error".format(tc))
    else:
        print("#{} error".format(tc))