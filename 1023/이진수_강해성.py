import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    number, s = input().split()
    #print(number, s)

    n = len(s)
    # print(s)
    bit = ""

    for i in range(n):
        d = ord(s[i]) - ord('0') if '0' <= s[i] <= '9' else ord(s[i]) - ord('A') + 10
        for j in range(3, -1, -1):
            bit += '1' if d & (1 << j) else '0'
    print("#{} {}".format(tc, bit))