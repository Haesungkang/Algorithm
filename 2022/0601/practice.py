import sys
sys.stdin = open('./inputfolder/input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    answer = 'impossible'
    num = int(input())
    for i in range(2, 10):
        if set(str(num)) == set(str(num * i)):
            answer = 'possible'
            break
    print("#{} {}".format(test_case, answer)) 