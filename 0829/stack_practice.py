arr = input()
stack = []

for str in arr:
    if str == "{" or str == "("
        stack.append(str)
    if str == "}" or str == ")"
        if len(stack) == 0:
            break
        t = stack.pop()
        if (str == ")" and t != "(") or (str == "}" and t != "{"):
            break

    if len(stack) == 0:
