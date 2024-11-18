# Normalize list:
# you have a list of list of depth n. Write a program to normalize it.
# Input: [1,[2,4,[5,1,[3,4],[7,8,[1,2]]]
# Output: [1,2,4,5,1,3,4,7,8,1,2]

def normalize_list(nested_list):
    normalized = []
    for element in nested_list:
        if isinstance(element, list):
            normalized.extend(normalize_list(element))
        else:
            normalized.append(element)
    return normalized

def main():
    input_list = [1, [2, 4, [5, 1, [3, 4], [7, 8, [1, 2]]]]]
    output_list = normalize_list(input_list)
    print(output_list)
    
if __name__ == "__main__":
    main()