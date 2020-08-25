import sys
sys.stdin = open('sample_input_4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    #딕셔너리 사용
    count = {}.fromkeys(str1,0)  #str1을 이용해서 dict을 생성
    # print(count)
    for ch in str2: # str2를 순회하면서
        if ch in count: #dict에 현재의 글자가 있는지
            count[ch] += 1
    # print(count)
    print("#{} {}".format(tc, max(count.values()))) # 딕셔너리 values() : 딕셔너리 값들을 리턴
