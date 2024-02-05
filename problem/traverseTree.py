class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")

def get_leaf(node,res):
    if node:
        if node.left == None and node.right == None: res.append(node.val)
        get_leaf(node.left,res)
        get_leaf(node.right,res)

def get_leaf_iterative(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()

        if node:
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return res

# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Perform inorder traversal
print("Inorder Traversal:")
print(get_leaf_iterative(root))
res=[]
res.append