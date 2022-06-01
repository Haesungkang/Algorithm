import sys
sys.stdin = open('sample_input_3.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    arr2 = []
    arr3 = []
    for i in range(N):
        arr.append(input())

    for i in range(len(arr)):
        for w in arr:
            arr2.append(w[i])

    for i in range(N):
        arr3.append("".join(arr2[N*i:N*i+N]))

    for word in arr:
        for i in range(len(word)+1-M):
            if word[i:i+M] == (word[i+M-1:i:-1]+word[i]):
                print("#{} {}".format(tc, word[i:i+M]))
    for word in arr3:
        for i in range(len(word)+1-M):
            if word[i:i+M] == (word[i+M-1:i:-1]+word[i]):
                print("#{} {}".format(tc, word[i:i+M]))
