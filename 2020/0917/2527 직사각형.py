import sys
sys.stdin = open("input6.txt", "r")

def check(A,B,C,D):
    #점일때
    if A == C or B == D:
        return 3
    #범위에 벗어날때
    if A < C or B < D:
        return 0
    #선으로만날때
    if (A == C and B > D) or (A == C and B > D):
        return 2
    #직사각형으로 겹칠때
    if A > C and B > D:
        return 4

for i in range(4):
    arr = list(map(int, input().split()))
    #print(arr)
    result1 = check(arr[0],arr[1],arr[6],arr[7])
    result2 = check(arr[2],arr[3],arr[4],arr[5])
    if result1 + result2 >= 4:
        print("a")
    if result1 + result2 == 2:
        print("b")
    if result1 + result2 == 3:
        print("c")
    if result1 + result2 == 0:
        print("d")