""" Reversing a Doubly Linked List (DLL) in Python is a great exercise in pointer manipulation. Since each node has both next and prev pointers, reversing involves swapping these for every node and updating the head.

🧠 Core Steps
- Traverse the list.
- For each node, swap its next and prev.
- After traversal, update the head to the last processed node.

🧾 Python Implementation """
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_dll(head):
    current = head
    temp = None

    while current:
        # Swap next and prev
        temp = current.prev
        current.prev = current.next
        current.next = temp

        # Move to the next node (which is prev now)
        head = current
        current = current.prev

    return head

# Helper to print DLL
def print_dll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Build sample DLL: 1 <-> 2 <-> 3 <-> 4
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("Original DLL:")
print_dll(head)

reversed_head = reverse_dll(head)

print("Reversed DLL:")
print_dll(reversed_head)



""" ✅ Output
Original DLL:
1 2 3 4 
Reversed DLL:
4 3 2 1  """




