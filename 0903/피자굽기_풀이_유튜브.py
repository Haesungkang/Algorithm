import sys
sys.stdin = open("sample_input_2.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map (int, input().split())   #N 화덕의 크기, M 피자수
    pizza = [0] + list(map(int, input().split()))

    oven = [i for i in range(1, N+1)]  # 피자번호
    #oven = [[i,pizza[i]] for i in range(1, N + 1)]
    # remain = [[i,pizza[i]] for i in range(N+1, M)]
    pos = N + 1

    while len(oven) > 1:
        num = oven.pop(0)
        #num, cheeze = oven.pop(0)
        pizza[num] = pizza[num] // 2
        #cheeze = cheeze //2
        if pizza[num]:
            oven.append(num)
            #oven.append([num,cheeze])
        else:
            if pos <= M:
                oven.append(pos)
                #oven.append([pos, pizza[pos]])
                pos += 1
            #if remain:
                # oven.append(remain.pop(0))
                
    print(oven[0])


