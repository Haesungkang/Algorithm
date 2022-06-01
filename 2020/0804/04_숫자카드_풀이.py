import sys
sys.stdin = open('../0inputlist/input4.txt', 'r') # 파일로 인풋받기

T = int(input())
for tc in range(1, T+1):    #[1,2,3]
    N = int(input())
    arr = [0] * 10  # 10칸짜리 배열 선언/ 0으로 초기화 -> 숫자카운팅용도
    num = [int(n) for n in input()] # '49679' -> 하나를 읽어들인다음에 한숫자씩 n으로 넣고 n을 int형변환후 리스트전환
    print(num)
    for n in num:
        arr[n] = arr[n] + 1  # arr배열의 n번 인덱스의 데이터를 하나 증가
    print(arr)
    max_idx = 0                # 최대값의 위치를 저장
    for i in range(len(arr)):
        if arr[max_idx] < arr[i]:
            max_idx = i
        if arr[max_idx] == arr[i] and max_idx < i:
            max_idx = i
    # print(max_idx) # 9 -> 위치
    # print(arr[max_idx]) #2 -> 담겨져있는 데이터
    print("#{} {} {}".format(tc, max_idx, arr[max_idx]))











