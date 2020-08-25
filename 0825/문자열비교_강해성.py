import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def bruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N :
        if t[i] != p[j]: # 매칭에 실패하면
            i = i -j
            j = -1 # 24번행에서 +1하면 0으로 변경되므로 -> 첫번째 패턴문자로 이동
        i += 1
        j += 1
    if j == M : return i -M
    else: return -1


for tc in range(1,T+1):
    p = input()
    t = input()
    M = len(p)
    N = len(t)
    if bruteForce(p, t) == -1:
        print("#{} 0".format(tc))
    else:
        print("#{} 1".format(tc))


