# binary search

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        mid = lower + (upper - lower) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            if lower == mid:
                break
            lower = mid
        elif target < array[mid]:
            upper = mid
    return None

def main():
    arr = [1,2,3,4,6,8,9,11,13]
    ret = binary_search(arr, 8)
    if ret is None:
        print("search element is not available")
    else:
        print("Element is available " + str(ret) + " position")
    
if __name__ == "__main__":
    main()