import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, 11):
    M, N = map(int, input().split())
    numberlist = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],
                  [0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],
                  [0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    for _ in range(M):
        arr = list(map(int, input()))
        #print(arr)
        onen = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                onen = i
        #print(onen)
        li = 0
        if onen != 0:
            li = (onen - 56)
            arr2 = arr[li+1:onen+1]
            #arr2 7개씩 쪼개서 확인
            lastsum = 0
            lastsum2 = 0

            for i in range(8):
                arr3 = arr2[7*i:7*i+7]
                #print(arr3)

                for j in range(len(numberlist)):
                    last = 8 - i
                    if arr3 == numberlist[j]:
                        lastsum2 += j
                        if last % 2 == 0:
                            lastsum += 3 * j
                        else:
                            lastsum += j


                        #last += ( 10 ** (7-i) ) * (j+1)
            #print(last)
            Final= True
            if lastsum % 10 == 0:
                Final = True
            else:
                Final = False

    if Final:
        print("#{} {}".format(tc, lastsum2))
    else:
        print("#{} 0".format(tc))




