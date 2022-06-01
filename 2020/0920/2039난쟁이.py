import sys
sys.stdin = open("input.txt", "r")

# 조합함수
def comb(n,r):
    global h
    if r == N:
        result = sum(h) - sum(sel)
        #만약 난쟁이의 합이 100이면 출력
        if result == 100:
            h.remove(sel[0])
            h.remove(sel[1])
            finalresult = sorted(h)
            for i in finalresult:
                print(i)
        return
    elif n >= len(h):
        return
    sel[r] = h[n]
    comb(n+1, r+1)
    comb(n+1, r)
# list추가
h = []
for i in range(9):
    h.append(int(input()))
# 9명중 2을 뺸 나머지를 조합해서 계산한다
N = 2
sel = [0] * 2
comb(0,0)



