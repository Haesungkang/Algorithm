import sys
sys.stdin = open('sample_input_4.txt', 'r')

def search(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return (2*search(n-2) + search(n-1))

T = int(input())

for tc in range(1, T+1):
    t = (int(input())//10)
    result = search(t)
    print("#{} {}".format(tc,result))