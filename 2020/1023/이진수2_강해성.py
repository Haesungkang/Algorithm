import sys
sys.stdin = open('input4.txt', 'r')

T = int(input())


for tc in range(1, T+1):
    number = float(input())
    #print(number)
    i = 0
    result = []
    while i < 13:
         if number >= (2**(-i)):
             number -= 2**(-i)
             result.append(i)
         if number == 0.0:
             break
         i += 1
    if number != 0.0:
        print('#{} overflow'.format(tc))
    else:
        n = result[-1]
        finalresult = [0] * (n)
        for i in result:
            finalresult[i-1] = 1
        print("#{} {}".format(tc,''.join(map(str,finalresult))))

