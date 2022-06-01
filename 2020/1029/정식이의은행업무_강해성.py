import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    a = list((input()))
    b = list((input()))

    anumber = bnumber = 0
    n = len(a)
    m = len(b)
    for i in range(len(a)):
        if a[i] != 0:
            anumber += 2 ** (len(a)-1-i) * (int(a[i]))

    for i in range(len(b)):
        if b[i] != 0:
            bnumber += 3 ** (len(b)-1-i) * (int(b[i]))

    #print(anumber, bnumber)
    # 2진수에서 하나씩 바꾸기
    numberlist2 = []
    for i in range(len(a)):
        if a[i] == '0':
            anumber2 = anumber + 2 ** (len(a)-1-i) * (1)
            numberlist2.append(anumber2)
        else:
            anumber3 = anumber - 2 ** (len(a)-1-i) * (int(a[i]))
            numberlist2.append(anumber3)
    #print(numberlist2)

    # 3진수 하나씩 바꾸기
    numberlist3 = []
    for i in range(len(b)):
        if b[i] == '0':
            # 1 승바꾸기
            anumber2 = bnumber + 3 ** (len(b)-1-i) * (1)
            numberlist3.append(anumber2)
            # 2 승 바꾸기
            anumber3 = bnumber + 3 ** (len(b) - 1 - i) * (2)
            numberlist3.append(anumber3)
        elif b[i] == '1':

            anumber2 = bnumber - 3 ** (len(b) - 1 - i) * (1)
            numberlist3.append(anumber2)
            # 2 승 바꾸기
            anumber3 = bnumber + 3 ** (len(b) - 1 - i) * (1)
            numberlist3.append(anumber3)

        else:
            anumber2 = bnumber - 3 ** (len(b) - 1 - i) * (1)
            numberlist3.append(anumber2)
            # 2 승 바꾸기
            anumber3 = bnumber - 3 ** (len(b) - 1 - i) * (2)
            numberlist3.append(anumber3)

    #print(numberlist3)

    X = len(numberlist2)
    Y = len(numberlist3)

    for i in range(X):
        for j in range(Y):
            if numberlist2[i] == numberlist3[j]:
                print("#{} {}".format(tc, numberlist2[i]))

    # subnumber = abs(anumber - bnumber)
    # result = 0
    # for i in range(n):
    #     for l in range(2):
    #         for j in range(m):
    #             for k in range(3):
    #                 if 2 ** (i) * l + 3 ** (j) * k == subnumber:
    #                     a[n-1-i] = str(l)
    #                     print(a)
    #
    #                     for i in range(len(a)):
    #                         if a[i] != 0:
    #                             result += 2 ** (len(a) - 1 - i) * (int(a[i]))

    # print("#{} {}".format(tc, result))





