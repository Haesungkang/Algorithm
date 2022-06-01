import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = input()
    S = []
    
    # 한문자씩 읽어서 처리
    ans = 1
    for ch in arr:
        if ch == '(' or ch == '{':
            S.append(ch)
        if ch == ')' or ch == '}':
            # 빈스택일경우
            if len(S) == 0:
                ans = 0; break
            t = S.pop()
            if (ch == ')' and t != '(') or (ch == '}' and t != '{'):
                ans = 0; break
        # else: #안해도된다
    if len(S) != 0: # 빈스택인지조사
        ans = 0
    print(ans)

# dictionary 사용
# paren = { '(' : ')', '{':'}', ')':'(', '}':'{'}
# for tc in range(1, int(input())+1):
#     arr = input()
#
#     S = []
#     # 한문자씩 읽어서 처리
#     ans = 1
#     for ch in arr:
#         if ch == '(' or ch == '{':
#             S.append(ch)
#         if ch == ')' or ch == '}':
#             # 빈스택일경우
#             if len(S) == 0:
#                 ans = 0; break
#             t = S.pop()
#             if paren[ch] != t:
#                 ans = 0; break
#         # else: #안해도된다
#     if len(S) == 0: # 빈스택인지조사
#         ans = 0
#     print(ans)
