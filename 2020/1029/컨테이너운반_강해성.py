import sys
sys.stdin = open('sample_input_2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 컨테이너 수 N과 트럭 수 M
    N, M = map(int, input().split())
    #  N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti
    # 얘를 옮겨야하고
    arrN = sorted(list(map(int, input().split())))
    # 얘는 옮길수있는 숫자이고
    arrM = sorted(list(map(int, input().split())))

    m = len(arrM)
    n = len(arrN)

    result = []
    while arrN:
        compare = arrN.pop()
        for i in range(len(arrM)-1, -1, -1):
            if arrM[i] >= compare:
                result.append(compare)
                del arrM[i]
                break

    print("#{} {}".format(tc, sum(result)))

    #print(arrN, arrM)

