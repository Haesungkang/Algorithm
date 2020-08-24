import sys
sys.stdin = open('../0inputlist/GNS_test_input.txt','r')

TC = int(input())
for case in range(TC):
    # 동시에 입력받기
    CASE_num, CASE_vol = map(str, input().split())
    # str인 CASE_vol을 int로 바꾸기: 직접 구현해보자!
    # CASE_vol = int(CASE_vol)
    def atoi(str):
        temp = 0
        for i in str:
            digit = ord(i) - ord('0')
            temp = temp*10 + digit
        return temp
    CASE_vol = atoi(CASE_vol)
    # CASE 입력받기:
    CASE = list(map(str, input().split()))
    # new_CASE에 문자->숫자로 변환하기:
    GNS = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    new_CASE = []
    for i in range(0, CASE_vol):
        num = CASE[i]
        digit = GNS[num]
        new_CASE.append(digit)
    # int list인 new_CASE 정렬하기: counting sort 사용해보자! 카운팅정렬 이해하기가 목표
    def counting_sort(input_array, max_num):
        # counting_sort는 입력받는 숫자의 최댓값을 알아야 한다!
        # 각 인덱스에 해당되는 숫자의 갯수를 세어 담을 counting_array 설정
        # 0부터 max_num까지의 숫자를 담아야 하므로 배열의 크기는 max_num+1로 설정
        counting_array = [0]*(max_num+1)
        # input_array에서 개별 요소들을 세, counting_array에 입력하자
        for num in input_array:
            counting_array[num] += 1
        # counting_array의 내용물을 갯수에서 좌표값으로 업데이트하자
        for i in range(1, max_num):
            counting_array[i] += counting_array[i-1]
        # output_array를 생성하자!
        # input_array만큼의 길이를 가진 리스트를 생성, 이 리스트에는 아직 입력되지 않은 칸에 -1 입력!
        output_array = [-1] * (len(input_array))
        # input_array에서의 숫자를 하나씩 짚어가며, counting_array를 참조해서 해당 값이 가진 좌표값을 찾는다.
        # 이 좌표값을 반영하여 해당 숫자를 output_array에 입력하고, 좌표값은 하나 줄여준다.
        for num in input_array:
            index = counting_array[num]
            # output_array는 0부터 시작하므로, index아닌 index-1임에 집중!
            output_array[index-1] = num
            counting_array[num] -= 1
        return output_array
    # new_CASE의 숫자들을 counting_sort로 정렬하자!
    sorted_new_CASE = counting_sort(new_CASE, 9)
    # GNS 딕셔너리를 반대로 뒤집고, 이를 참조해 숫자 -> 문자로 변환해 CASE에 입력
    reverse_GNS = {value:key for key, value in GNS.items()}
    sorted_CASE = []
    print(reverse_GNS)
    # print(CASE_vol)
    print(sorted_new_CASE)
    print(num)
    # for i in range(0, CASE_vol):
    #     digit = sorted_new_CASE[i]
    #     num = reverse_GNS[digit]
    # #     sorted_CASE.append(num)
    # print(num)
    # # 이대로 print(sorted_CASE 하면 [] 내에 출력돼서 나온다! []도 지우고 ''도 지워보자)
    # print(CASE_num)
    # # print(sorted_new_CASE)
    # for i in range(CASE_vol):
    #     print(sorted_CASE[i], end=' ')