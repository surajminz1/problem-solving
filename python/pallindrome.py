# Print fibonacci series

def is_pallindrome(string):
    rev = "".join(reversed(string))
    if string == rev:
        return True
    else:
        return False

def main():
    string = "root"
    string2 = "sanas"
    print(is_pallindrome(string))
    print(is_pallindrome(string2))
    
if __name__ == "__main__":
    main()