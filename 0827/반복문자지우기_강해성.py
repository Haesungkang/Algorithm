import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    text  = list(input())
    stack = []
    for i in range(len(text)):
        if len(stack) == 0 or stack[-1] != text[i]:
            stack.append(text[i])
        else:
            stack.pop()

    print("#{} {}".format(tc, len(stack)))

    # while i < len(text)-1:
    #     if text[i] == text[i+1]:
    #         text.remove(text[i+1])
    #         text.remove(text[i])
    #         i = 0
    #     else:
    #         stack.append[]
