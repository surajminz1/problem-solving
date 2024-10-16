# Search a given element x in an array arr[] of n elements

def search(arr, n):
    i = 0
    for i in range(len(arr)):
        if n == arr[i]:
            return i
    
    print("element not found")

def main():
    arr = [3,6,8,4,1,9,2]
    print(search(arr, 4))
    
if __name__ == "__main__":
    main()