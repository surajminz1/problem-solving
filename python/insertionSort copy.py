def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
"""
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)  # Output: [5, 6, 11, 12, 13]
"""
A = [5,4,3,7,2]
print(A)
insertion_sort(A)
print(A)