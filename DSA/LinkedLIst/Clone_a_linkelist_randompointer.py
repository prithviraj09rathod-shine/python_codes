class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.random = None

def clone_linked_list(head):
    if not head:
        return None

    # Step 1: Insert cloned nodes next to original nodes
    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Set random pointers for cloned nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate original and cloned lists
    original = head
    clone = head.next
    clone_head = clone

    while original:
        original.next = original.next.next
        clone.next = clone.next.next if clone.next else None
        original = original.next
        clone = clone.next

    return clone_head
###################################
#simple way to copy ll with random pointer using hashmap
def clone_linked_list_hashmap(head):
    if not head:
        return None

    old_to_new = {}

    # First pass: create all nodes and store them in the hashmap
    current = head
    while current:
        copy = Node(current.data) ## create new node amd do deepcopy of data
        old_to_new[current] = copy
        current = current.next

    # Second pass: assign next and random pointers
    current = head
    while current:
        copy = old_to_new[current]
        if current.next:
            #copy = old_to_new[current] # will give the copied node
            copy.next = old_to_new[current.next] # next of original node i.e current.next will give the next node of copied node i.e copy
            #old_to_new[current].next = old_to_new[current.next]
        if current.random:
            #old_to_new[current].random = old_to_new[current.random]
            copy.random = old_to_new[current.random]
        current = current.next

    return old_to_new[head]
# Create original list: 1 → 2 → 3
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

# Set random pointers
a.random = c
b.random = a
c.random = b
 
# Clone the list
#cloned_head = clone_linked_list(a)
cloned_head = clone_linked_list_hashmap(a)

# Print cloned list
def print_list(head):
    while head:
        rand = head.random.data if head.random else None
        print(f"Node({head.data}) → Random({rand})")
        head = head.next

print("Cloned Linked List:")
print_list(cloned_head)

#Cloned Linked List:
""" Node(1) → Random(3)
Node(2) → Random(1)
Node(3) → Random(2) """