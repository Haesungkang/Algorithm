import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 먼저 전체순회를 해서 값이 다른 16진수들의 마지막 idx와 값들을 먼저 list에 각각 넣어주기

    # 그리고 나서 그 행 값들 전부 뽑아내서 2진수로 바꾸기

    # 2진수로바꾼다음에 이것들이 56의 배수 판단해주기

    # 56배수에 따라서 그에따른 값들 하나씩 암호코드 스캔해주기


    #각행마다
    for row in arr:
        bit = ""
        for i in row:
            if '0' <= i <= '9':
                d = ord(i) - ord('0')
            else:
                d = ord(i) - ord('A') + 10

            for j in range(3, -1, -1):
                if d & (1 << j):
                    bit += '1'
                else:
                    bit += '0'
        #일단 2진수 전부 만들어내기

        print(bit)
        # bitidx = 0
        # bitidx2 = 0
        # for i in range(len(bit)):
        #     if bit[i] == '1':
        #         bitidx = i
        # for i in range(bitidx, -1, -1):
        #     if bit[i] == '1':
        #         bitidx2 = i
        # if bitidx - bitidx2 != 0:
        #     print(bitidx - bitidx2)

    print()
    # for i in range(N-1,-1,-1):
    #     for j in range(M-1,-1,-1):
    #         if arr[i][j] != "0":
    #             print(i, j)
    #             break
    #     break
    # for row in arr:
    #     print(row)