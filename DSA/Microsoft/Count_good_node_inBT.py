class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class solution:
    def count_good_nodes(self, root:TreeNode)->int:
        def dfs(node, maxVal_so_far):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal_so_far else 0
            maxVal_so_far = max(maxVal_so_far, node.val)
            res += dfs(node.left, maxVal_so_far)
            res+= dfs(node.right, maxVal_so_far)
            return res
        return dfs(root, root.val)
    

#input = [3,1,4,3,None,1,5]
# Construct the tree: [3,1,4,3,null,1,5]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

#example 2
root1 = TreeNode(3)
root1.left = TreeNode(3)
root1.left.left= TreeNode(4)
root1.left.right = TreeNode(2)

obj = solution()
obj.count_good_nodes(root)
print("Number of good nodes:", obj.count_good_nodes(root))  # Output: 4
print("Number of good nodes:", obj.count_good_nodes(root1))  # Output: 
#expected output = 4