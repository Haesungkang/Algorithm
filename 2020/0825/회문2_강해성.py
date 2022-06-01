import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    t = int(input())
    arr = []
    arr2 = []
    arr3 = []

    for i in range(100):
        arr.append(input())

    for i in range(100):
        for w in arr:
            arr2.append(w[i])
    for i in range(100):
        arr3.append("".join(arr2[100*i:100*i+100]))

    max_length = 1

    for word in arr:
        for length in range(100):
            for idx in range(101-length):
                if word[idx:idx+length] == (word[idx:idx+length][::-1]):
                    if max_length <= len(word[idx:idx+length]):
                        max_length = len(word[idx:idx+length])

    for word in arr3:
        for length in range(1, 100):
            for idx in range(101-length):
                if word[idx:idx+length] == (word[idx:idx+length][::-1]):
                    if max_length <= len(word[idx:idx + length]):
                        max_length = len(word[idx:idx + length])
    print("#{} {}".format(tc, max_length))
