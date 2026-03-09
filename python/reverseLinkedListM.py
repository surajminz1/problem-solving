# Implement a function to reverse a linked list (you don't need to define a full linked list class, just the logic).
# Complexity: \
# Desired time: <8mins
# Time taken to solve: 15 mins

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_link_list_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_link_list_recursive(self):
        def _reverse_link_list_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_link_list_recursive(next_node, current)
        self.head = _reverse_link_list_recursive(self.head, None)

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

# Example usage:
def main():
    llist = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        llist.append(value)
    print("Original Linked List:")
    print(llist)

    llist.reverse_link_list_iterative()
    print("\nReversed Linked List (Iterative):")
    print(llist)

    llist.reverse_link_list_recursive()
    print("\nReversed Linked List (Recursive):")
    print(llist)
    
if __name__ == "__main__":
    main()