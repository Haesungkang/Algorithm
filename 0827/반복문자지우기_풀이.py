for tc in range(1, int(input())+1):
    arr = input()
    S = []

    for ch in arr:
        if not S:
            S.append(ch) # 빈상태인경우는 항상 체크해주는 것이 좋다
        elif ch != S[-1]:
            S.append(ch) #빈스택이 아닌경우는 ch 와 S[-1]과 비교해서 다르면 stack에 push하기

        # 앞에것이 false이면은 뒤에것을 보는데 앞에것이 true이면은 넘어가니깐 주의하기 줄일때 어떻게 줄일때 생각해보기
        # if not S or ch != S[-1]:
        #     S.append(ch)

        else:
            S.pop() #같으면 ch와 S[-1]을 버린다

    print(len(S))