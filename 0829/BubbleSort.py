def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i): # bubble sort의 개념을 다시 생각해보면서 i가 왜들어가는지 생각해보기
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
