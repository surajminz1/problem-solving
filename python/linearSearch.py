# Strings:
# write code to reverse words in sentence

def linear_search(num_arr, x):
    for i in range(0, len(num_arr)):
        if num_arr[i] == x:
            return i
    return -1

def main():
    # Example usage:
    arr_num = [4, 5, 3, 7, 2, 9]
    x = 7
    result = linear_search(arr_num, x)
    if(result == -1):
        print("Not present in arrray")
    else:
        print("Present in arrray")

if __name__ == "__main__":
    main()