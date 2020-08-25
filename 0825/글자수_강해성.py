import sys
sys.stdin = open('sample_input_4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    Str = input()
    Str2 = input()
    count = [0 for _ in range(26)]
    count2 = [0 for _ in range(26)]
    for ch in Str:
        n = ord(ch) - ord("A")
        count[n] += 1
    for ch in Str2:
        n = ord(ch) - ord("A")
        count2[n] += 1
    # print(count)
    # print(count2)
    max = 0
    maxidx = 0
    for i in range(len(count)):
        if count[i] != 0 and count2[i] !=0:
            if max < count2[i]:
                maxidx = i
                max = count2[i]
    print("#{} {}".format(tc, max))