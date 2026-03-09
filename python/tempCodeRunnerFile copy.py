def find_indices(arr, target):
    if target in arr:
        print(arr.index(target))
        return [arr.index(target), len(arr) - 1 - arr[::-1].index(target)]
    return [-1, -1]

# Test cases
print(find_indices([2, 4, 7, 7, 7, 9, 10], 7))   # [2, 4]
#print(find_indices([2, 4, 7, 7, 7, 9, 10], 11))  # [-1, -1]
#print(find_indices([2, 4, 7, 7, 7, 9, 10], 4))   # [1, 1]


