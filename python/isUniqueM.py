# Write a function that takes a list of integers and returns a new list containing only the unique elements in the original list, preserving the original order.
# Complexity: O(n Log n), because inbuilt sorting algorithm is used
# Desired time: < 4mins
# Time taken to solve 6 mins

def is_unique(lst):
    seen = set()
    uni_lst = []
    for num in lst:
        if num not in seen:
            uni_lst.append(num)
            seen.add(num)

    return uni_lst

def main():
    # Example usage:
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = is_unique(numbers)
    print(unique_numbers)

if __name__ == "__main__":
    main()