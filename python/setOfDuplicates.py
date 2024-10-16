# Print set of duplicates in a list

def main():
    lst = [1,2,3,4,4,5,6,6,7,8,8,9]
    print(set([x for x in lst if lst.count(x) > 1]))
    
if __name__ == "__main__":
    main()