a = [1,'c',(1,2),{'b': 0}, True, 4.5],[1,2,3]
print(a)
## Output: ([1, 'c', (1, 2), {'b': 0}, True, 4.5], [1, 2, 3])

# Create list of numbers with given range
r1 = 0
r2 = 10

  ### using list comprehension
li = [i for i in range(r1,r2)]
print(li)
## Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  ### using range()
li = list(range(r1,r2))
print(li)
## Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ways to create a dictionary of Lists - Python
d = {}
d["1"] = [1,2]
d["2"] = ["Geeks","For","Geeks"]
print(d)
## Output: {'1': [1, 2], '2': ['Geeks', 'For', 'Geeks']}

  ### using the zip()
k = ["Fruits", "Vegetables", "Drinks"]
val = [["Apple", "Banana"], ["Carrot", "Spinach"], ["Water", "Juice"]]
d = dict(zip(k,val))
print(d)
## Output: {'Fruits': ['Apple', 'Banana'], 'Vegetables': ['Carrot', 'Spinach'], 'Drinks': ['Water', 'Juice']}

  ### using 

# Create a List of Tuples in Python


# How to create list of dictionary in Python


# Create List of Size n


# Create a List of Strings in Python


# Create a list of tuples from given list having number and its cube in each tuple


# Create a List of Floats


# Create Dictionary from List with Default Values


# Create list of numbers with given range


# Ways to create a dictionary of Lists - Python


# Create List of Size n


# Create dictionary from the list


# Create a list of tuples from given list having number and its cube in each tuple


# Create Nested Dictionary using given List


# How to Create List of Dictionary in Python Using For Loop


# Create a List of Floats


# Create nested list containing values as the count of list items


# Ways to create triplets from given list


# Randomly create N Lists of K size


# Create a list centered on zero

