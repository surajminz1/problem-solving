# write a program to find the total number of anagrams in a list
# Input: ["ate","inch","eat","tac","tea","cat","chin"]
# Output: 3
# (ate, eat, tea), (cat, tac), (inch, chin)

def findAnagram(arr):
    arr_dic = {}
    for item in arr:
        item_sort = "".join(sorted(item))
        if item_sort in arr_dic:
            arr_dic[item_sort] += 1
        else:
            arr_dic[item_sort] = 1
    print(len(arr_dic))
    print(arr_dic)

def main():
    arr = ["ate","inch","eat","tac","tea","cat","chin","abc"]
    findAnagram(arr)
    
if __name__ == "__main__":
    main()