T = input()
T_list = list(T)
sum = 1
for T in range(len(T_list)):
    if T_list[T] == ' ':
        sum +=1
if T_list[0] == ' ':
    sum -= 1
if T_list[len(T_list)-1] == ' ':
    sum -= 1
print(sum)

