from typing import Optional


class TreeNode:
    def __intit__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class solution:
    def post_order_traversal(self, root: Optional[TreeNode])->list[int]:
        stack  = [root]
        visit = [False]
        res = []

        while stack:
            curr, v = stack.pop(), visit.pop()
            if curr:
                if v:
                    res.append(curr.value)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append{False}

