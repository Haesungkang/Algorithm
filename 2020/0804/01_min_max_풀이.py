# min/max함수를 사용하지않고 구현
# 정렬해서 푸는방법도 있지만 이문제에서는 필요가 없음
'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

def find(a, n):
    # 최대/최소값 초기설정
    maxValue = a[0]     # 극최소값 : 0
    minValue = a[0]     # 극최대값 : 9999999
    for i in range(1, n):   #모든값을 순회한다
        if a[i] > maxValue:
            maxValue = a[i]
        if a[i] < minValue:
            minValue = a[i]
    # 최대값 - 최소값
    return maxValue - minValue

T = int(input())
for tc in range(1, T+1):
    #입력
    N = int(input())
    v = list(map(int,input().split()))
    #계산
    #출력
    print("#{} {}".format(tc, find(v, N)))
