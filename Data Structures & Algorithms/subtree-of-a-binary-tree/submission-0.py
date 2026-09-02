# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        if s.val != t.val:
            return False

        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        