from typing import Optional
class TreeNode:
    def __init__(self, value:0,left:None, right:None):
        self.value = value
        self.lef = left
        self.right = right

class solution:
    def deleteNode(self, root:Optional[TreeNode], key:int)->Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.value:
            root.right = self.deleteNode(root.right, key)
        elif key < root.value:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            #find min from right subtree
            curr = root.right

            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.value)
        return root


obj = solution()
obj.deleteNode() 
print(obj.deleteNode())
