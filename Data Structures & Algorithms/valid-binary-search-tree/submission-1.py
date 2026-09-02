# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inOrder(root)

    def inOrder(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if not self.inOrder(root.left):
            return False
        
        if self.prev is not None and root.val <= self.prev:
            return False
        
        self.prev = root.val
        return self.inOrder(root.right)


