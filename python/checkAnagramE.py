# Given two strings, write a function to check if one is an anagram of the other.
# Complexity: O(n Log n), because inbuilt sorting algorithm is used

def check_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "") # Normalize strings to lowercase and remove spaces
    str2 = str2.lower().replace(" ", "")
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)

def main():
    # Example usage:
    print(check_anagram("listen", "silent"))  # True
    print(check_anagram("hello", "world"))   # False

if __name__ == "__main__":
    main()