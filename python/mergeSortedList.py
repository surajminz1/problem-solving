# Iterator:
# write code to iterate on an iterator

def merge_sorted_lists(lists):
    merged_list = []
    
    # Create indices to keep track of the current position in each list
    indices = [0] * len(lists)
    print("indices : ",indices)
    
    while True:
        min_value = None
        min_index = -1
        
        # Find the smallest element among the lists
        for i in range(len(lists)):
            if indices[i] < len(lists[i]):
                print(indices[i]," ",lists[i])
                print(lists[i][indices[i]])
                if min_value is None or lists[i][indices[i]] < min_value:
                    print(lists[i][indices[i]]," min_value: ",min_value)
                    min_value = lists[i][indices[i]]
                    min_index = i
                    print("min_value: ",min_value," min_index: ",min_index)
        
        # If all lists are exhausted, break the loop
        if min_value is None:
            break
        
        # Add the smallest element to the merged list
        merged_list.append(min_value)
        print("merged_list: ",merged_list)
        # Move the index of the list from which the smallest element was taken
        indices[min_index] += 1
        print("indices[min_index]: ",indices[min_index])

    return merged_list

def main():
    # Example usage:
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(merge_sorted_lists(lists))


if __name__ == "__main__":
    main()