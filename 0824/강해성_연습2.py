# import collections

T = input()
t = T.upper()
t_list = list(t)
# counting = collections.Counter(t_list)

print(counting)
dict_max = max(counting.values())
max_list = []
for key, value in counting.items():
    if value == dict_max:
        max_list.append(key)

if len(max_list) > 1:
    print('?')
else:
    print(max_list[0])