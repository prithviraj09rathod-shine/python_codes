""" To convert a Binary Tree (BT) to a Binary Search Tree (BST) in Python,
the structure of the tree remains the same, 
but the node values are rearranged to satisfy the BST property: left < root < right.

🧠 Strategy
- Traverse the binary tree and store all node values.
- Sort the values.
- Reassign the sorted values back to the tree using an in-order traversal. """


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Step 1: Store values from the binary tree
def store_inorder(node, values):
    if node is None:
        return
    store_inorder(node.left, values)
    values.append(node.data)
    store_inorder(node.right, values)

# Step 2: Assign sorted values back to the tree
def assign_inorder(node, values, index):
    if node is None:
        return index
    index = assign_inorder(node.left, values, index)
    node.data = values[index]
    index += 1
    index = assign_inorder(node.right, values, index)
    return index

# Main function to convert BT to BST
def binary_tree_to_bst(root):
    values = []
    store_inorder(root, values)
    values.sort()
    assign_inorder(root, values, 0)

# Helper to print in-order traversal
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.data, end=' ')
        print_inorder(node.right)

# Sample Binary Tree
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

print("Original Binary Tree (Inorder):")
print_inorder(root)

binary_tree_to_bst(root)

print("\nConverted BST (Inorder):")
print_inorder(root)