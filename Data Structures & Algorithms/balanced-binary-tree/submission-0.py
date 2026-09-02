# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, node) -> int:
        if node is None:
            return 0

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        return max(left_height, right_height) + 1

        