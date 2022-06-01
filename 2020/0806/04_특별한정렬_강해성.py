import sys
sys.stdin = open('sample_input.txt', 'r')

# 먼저 Sort하는 함수를 제작합니다
def selectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selectionSort(arr)
    #Sort한 list중에서 이제 원하는대로 값을 넣어줍니다
    #기본 blanklist를 만들어서 거기에 따른 값들을 넣어줍니다
    finallist =[0]* len(arr)
    for i in range(int(len(arr)/2)):
        finallist[i*2+1] =  arr[i]
        finallist[2 * i] = arr[len(arr)-1-i]
    # 그중에서 10번째까지만 출력할수있게 자른다음에 str변환후 join시켜 list를 출력
    result = map(str, finallist[:10])
    finalresult = ' '.join(result)

    print("#{} {}".format(tc, finalresult))


