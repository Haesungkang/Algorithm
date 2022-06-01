import sys
sys.stdin = open("sample_input_4.txt", "r")

# perm(k)로 진행할경우 크기가 엄청커져서 결국 진행이 안될수도있다 그래서
# cursum을 통해서 0~k-1행에 선택한 값들의 합을 추가한다
def perm(k, cur_sum):
    global ans;
    # 만약에 숫자가 크면 끝내기 = 이밑에있는부분은 다음함수 넘어가기전에 아무데나 넣어도 상관이 없다
    if ans <= cur_sum : return

    if k == N:
        ans = min(ans, cur_sum)
        # 첫번째 시간좀오래걸리는법
        # S = 0
        # for r, c in enumerate(cols):
        #     S += arr[r][c]
        # global ans; ans = min(ans, S)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1, cur_sum + arr[k][cols[k]])
            arr[k], arr[i] = arr[i], arr[k]



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0,0)
    print(ans)
