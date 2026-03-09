# Implement a function to reverse a linked list (you don't need to define a full linked list class, just the logic).
# Complexity: 
# Desired time: 
# Time taken to solve:

"""
Sample Input:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
"""

n = int(input())
set_a = set(map(int, input().split()))

# Input the number of other sets
num_operations = int(input())
j = 0
# Execute each operation
for i in range(num_operations):
    # Read the operation name and length of the other set
    operation, i = input().split()
    print("operations & i: ", operation, i)
    # Read the other set
    other_set = set(map(int, input().split()))
    print("other_set: ", other_set)
    # Perform the operation on set_a
    x = getattr(set_a, operation)(other_set)
    print(type(set_a))

# Output the sum of elements in set_a
print(sum(set_a))
