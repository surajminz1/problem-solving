def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        print(curNum)
        for j in range(i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
            print(A)

A = [5,4,3,7,2]
print(A)
print("After sorting: ", insertion_sort(A))