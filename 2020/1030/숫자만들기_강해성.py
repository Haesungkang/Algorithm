import sys, math
sys.stdin = open('sample_input.txt', 'r')


def calll(sel, cal):
    while cal:
        #print(sel)
        #print(cal)
        a = sel.pop(0)
        b = sel.pop(0)
        #print(a, b)
        c = cal.pop(0)
        if c == '+':
            d = a + b
            sel.insert(0,d)
        elif c == '-':
            d = a - b
            sel.insert(0,d)
        elif c == '*':
            d = a * b
            sel.insert(0,d)
        else:
            d = math.trunc(a / b)
            sel.insert(0,d)

    return sel[0]

def perm(k):
    global finalresult2, finalresult1
    if k == N:
        sel2 = sel[:]
        arr2 = arr[:]
        result = calll(arr2, sel2)
        if finalresult1 < result:
            finalresult1 = result
        if finalresult2 > result:
            finalresult2 = result
        return
    for i in range(N):
        if visited[i] == 0:
            sel[k] = callist[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    cal = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    comblist = []
    # index 안에 있는 숫자만큼 더하기
    calcal = ['+', '-', '*', '//']
    callist = []
    for i in range(len(cal)):
        while cal[i] > 0:
            callist.append(calcal[i])
            cal[i] -= 1

    N = len(callist)
    sel = [0] * N
    visited = [0] * N
    finalresult1 = -999999999
    finalresult2 = 100000
    perm(0)
    #N = len(callist)

    #print(comblist)
    #print(arr)
    # for i in comblist:
    #     if len(i) == N:
    #         arr2 = arr[:]
    #         if finalresult1 < calll(arr2, i):
    #             finalresult1 = calll(arr2, i)
    #         if finalresult2 > calll(arr2, i):
    #             finalresult2 = calll(arr2, i)

    print("#{} {}".format(tc, finalresult1 - finalresult2))







