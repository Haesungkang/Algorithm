T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    move = 0
    chung = 0
    # Move는 차가 충전기로 움직이는 방향
    # chung은 충전횟수를 지정한다
    for mm in range(int(N/K)+10):
        move += K
        result1 = []
        # move를 하면서 그안에 값들을 차곡차곡쌓은다음에 마지막값을로 이동
        for i in arr:
            if move >= i:
                result1.append(i)
        #만약 move가 정류장길이보다 크거나 같으면 바로 break하고 출력
        if move >= N:
            print('#{} {}'.format(tc, chung))
            break
        move = result1[-1]
        chung += 1

        # print(chung, move)
    # 계속 못지나가고있을경우 0 출력
    if move < N:
        print('#{} 0'.format(tc))

