import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # 카드 한덱을 저장하기 위한 배열 선언
    deck = [[0 for _ in range(13)] for _ in range(4)]
    types = ['S', "D", "H", "C"]
    cards = list(input())
    # print(cards)
    isError = False # 에러 발생여부 저장
    # 리스트에서 한자씩 꺼내서 작업
    # 리스트에 자료가 있는 동안 + 에러가 없는 동안 반복
    while cards and not isError:
        type = cards.pop(0) # 타입
        nums = cards.pop(0) # 첫번째 숫자
        nums = nums + cards.pop(0) # 두번쨰 숫자
        num = int(nums)

        for i in range(len(types)):
            if type = types[i]:
                if deck[i][num] == 0:   #아직 카드가 없을떄
                    deck[i][num] == 1
                else:   #카드가 중복
                    isError = True  #에러발생체크
                    break

    print("#%d" %tc, end=" ")
    if isError:
        print("ERROR")
    else:
        for row in deck:
            need = 0 #필요한 카드수 세기 (무늬별)
            for c in row:
                if c == 0:
                    need += 1
        print(need, end=" ")
        print()
