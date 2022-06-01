import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = list(input())
    stack = []
    falsetime = 0
    for i in range(len(text)):
        if text[i] == "(" or text[i] == "{":
            stack.append(text[i])
        elif text[i] == ")" or text[i] == "}":
            if len(stack) == 0:
                falsetime += 1
            else:
                check = stack.pop()
                if check == '(' and text[i] != ')':
                    falsetime += 1
                elif check == '{' and text[i] != '}':
                    falsetime += 1

    if len(stack) != 0 or falsetime != 0:
        print("#{} 0".format(tc))
    else:
        print("#{} 1".format(tc))

    # # print(stack)
    # stack2 = []
    # stack3 = []
    # for i in range(len(stack)):
    #     if stack[i] == "(" or stack[i] == ")":
    #         stack2.append(i)
    #     if stack[i] == "{" or stack[i] == "}":
    #         stack3.append(i)
    # # print(stack2)
    # # print(stack3)
    # L = len(stack2)//2
    # M = len(stack3)//2
    # falsetime = 0
    # # print(L, M)
    #
    # if len(stack2)%2 != 0 or len(stack3)%2 != 0:
    #     falsetime += 1
    # else:
    #     for i in range(L):
    #         if (stack2[len(stack2)-1-i] - stack2[i])%2 != 1:
    #             falsetime += 1
    #     for i in range(M):
    #         if (stack3[len(stack3)-1-i] - stack3[i])%2 != 1:
    #             falsetime += 1
    #
    # if falsetime != 0:
    #     print("#{} 0".format(tc))
    # else:
    #     print("#{} 1".format(tc))


