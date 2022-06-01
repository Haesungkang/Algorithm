import sys
sys.stdin = open("sample_input_2.txt", "r")

def inorder(n):
    global result
    if n <= N:
        inorder(n*2)
        result.append(n)
        inorder(n*2+1)



for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    number = [i for i in range(N+1)]
    result = [0]
    #print(number)
    inorder(1)
    #print(result)
    result1 = 0
    result2 = 0

    for i in range(len(result)):
        if result[i] == 1:
            result1 = number[i]
        if N//2 == result[i]:
            result2 = number[i]

    print("#{} {} {}".format(tc, result1, result2))
