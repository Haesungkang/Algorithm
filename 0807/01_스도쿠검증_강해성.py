import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def selection(a):
    falsecount = 0
    for num in range(1, 10):
        if a.count(num) != 1:
            falsecount += 1
    return falsecount

for tc in range(1,T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    false1 = 0

    for garo in arr:
       false1 += selection(garo)

    for sero in range(9):
        list1 =[]
        for i in range(9):
            list1.append(arr[i][sero])
        false1 += selection(list1)
    #3*3행렬 찾기
    list3 = []
    for last in range(3):
        for last2 in range(3):
            for i in range(3):
                for j in range(3):
                    list3.append(arr[3*last+i][3*last2+j])
    #3*3행렬 다같이 리스트로 나와서 쪼개는 작업
    list4 = []
    for i in range(9):
        list4.append(list3[9*i:9*i+9])
    for b in list4:
        false1 += selection(b)
    #결과값비교
    if false1 == 0:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))


