from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node, prev_max=float("-inf")):
            if not node:
                return None
            nonlocal res

            if prev_max<=node.val:
                res.append(node.val)

            prev_max = max(node.val, prev_max)

            if node.left:
                dfs(node.left, prev_max)
            
            if node.right:
                dfs(node.right, prev_max)
        
        dfs(root)
        return len(res)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
    
        def dfs(node):
            if not node:
                return 0
            nonlocal count
            sum = 0
            node = root
            while sum < targetSum:
                sum += node.val
                node = node.left



# # Define the binary tree
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
# root.left.right = None  # Assuming null is represented by None
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)

# Define the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

sol = Solution()
