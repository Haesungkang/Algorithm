import sys
sys.stdin = open('sample_input_4.txt', 'r')

def f(n): # n: 문제의 크기(식별값)
    #재귀호출을 할땐 매개변수를 보고 판단해야한다
    # 기저사례
    if n == 1: return 1
    if n == 2: return 3
    # 그냥해버릴경우 같은 것을 호출하는 경우가 많아진다
    # 그래서 memorization을 통해서 그 반복되는 경우를 줄여준다
    # f(n)일때는 n-1개의 값을 알면되면되자나

    # 일반사례
    if memo[n]: return memo[n]

    memo[n] = f( n - 1 ) + f( n - 2 ) * 2

    return memo[n]


for tc in range(1, int(input())+ 1):
    N = int(input()) // 10
    # memorization을 위해서 10으로 나눴다
    memo = [0] * (N+1) #초기값 0 --> 이문제의 답을 아직 구하지 않음

    print(f(N))

# 반복을 이용해서 푸는 방법
# memo = [0] * (30+1)
# memo[1], memo[2] = 1, 3
#
# for i in range(3, N + 1):  # i -> 문제의 크기를 나타내는 값
#     memo[n] = memo[i - 1] + memo[i - 2] * 2
#
# for tc in range(1, int(input())+ 1):
#     N = int(input()) // 10
#
#     print(memo[N])