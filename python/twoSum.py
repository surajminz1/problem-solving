# Two sum problem:
# Find pairs that add upto a target
# Input: [1,2,3,4], 5
# Output: [[2,3],[1,4]]

def find_pairs(arr_num, target):
    result = []
    used = []
    for i in range(len(arr_num)):
        leftover_num = target - arr_num[i]
        print(leftover_num)
        if leftover_num in arr_num and leftover_num not in used and arr_num[i] not in used:
            result.append([arr_num[i], leftover_num])
            print(result)
            used.append(leftover_num)
            used.append(arr_num[i])
            print("used: ", used)
    return result

def main():
    arr_num = [1,2,3,4]
    print(find_pairs(arr_num, 5))
    
if __name__ == "__main__":
    main()