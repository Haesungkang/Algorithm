a = int(input())
arr = list(map(int, input().split()))

#1
sum = 0
for i in arr:
    if i % 2 == 0:
        sum += 1
print(sum)

#2
sum2 = 0
for i in range(0, a-1):
    if arr[i] < arr[i+1]:
        sum2 += 1
print(sum2)

#3
sum3 = 0
for i in range(1, a):
     mini = min(arr[0:i])
     final = arr[i] - mini
     sum3 += abs(final)
print(final)

#4
# sum4 = 0
# for i in range()