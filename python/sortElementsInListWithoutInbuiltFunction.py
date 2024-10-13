# Sort elements in a list without using in-built function
def sort_elements_in_list_without_inbuilt_function(list_elem):
    new_list = []

    while list_elem:
        min = list_elem[0]
        for x in list_elem:
            if x > min:
                min = x
        new_list.append(min)
        list_elem.remove(min)
    return new_list

def main():
    list_elem = [78, 1,47,33,4,9,16,18,98,34,56,29]
    sorted = sort_elements_in_list_without_inbuilt_function(list_elem)
    print(sorted)

if __name__ == "__main__":
    main()