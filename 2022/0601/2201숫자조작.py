import sys
sys.stdin = open('./inputfolder/input5.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # input()을 받고나서 str한다음에 int 변환후 반환
    
    num = list(map(int, str(input())))
    #print(num)
    A, B = min(num), max(num)
    if A == 0:
        AA = list(set(sorted(num)))
        A = AA[1]
    #print(A, B)
    #최대값 만들기 
    list1 = []
    list1.append(num)
    num2 = num
    list1.append(num2)
    maxarr = list1[0]
    minarr = list1[1]
    #print(num)
    maxlist = 0
    minlist = 0
    for i in range(len(maxarr)):
        if maxarr[i] == A:
            maxlist = i
            break
    for j in range(len(maxarr)):
        if maxarr[j] == B:
            minlist = j
            break
    #print(maxlist, minlist)
    
    maxarr[i] = A
    maxarr[j] = B
    C = ''.join(map(str, maxarr))

    minarr[i] = B
    minarr[j] = A
    D = ''.join(map(str, maxarr))

    #원래는 CD 출력하려고했으나
    # 숫자가 반대일 경우 반대
    if D > C:
        print("#{} {} {}".format(tc, C, D))
    else:
        print("#{} {} {}".format(tc, D, C))



# from itertools import combinations

# t = int(input())

# for tc in range(1, t + 1) :
#     data = list(map(str, input()))
#     target = [i for i in range(len(data))]

#     min_value, max_value = int(''.join(data)), int(''.join(data))

#     for value in combinations(target, 2) :
#         i, j = value
#         data[i], data[j] = data[j], data[i]
#         if data[0] == '0' :
#             data[i], data[j] = data[j], data[i]
#             continue
#         if int(''.join(data)) < min_value :
#             min_value = int(''.join(data))
#         if int(''.join(data)) > max_value :
#             max_value = int(''.join(data))
#         data[i], data[j] = data[j], data[i]

#     print('#%d %d %d' % (tc, min_value, max_value))