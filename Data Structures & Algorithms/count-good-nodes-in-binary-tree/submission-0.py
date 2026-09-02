# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, float('-inf'))
    
    def countGoodNodes(self, node: TreeNode, max_so_far: int) -> int:
        if node is None:
            return 0
        
        count = 0

        if node.val >= max_so_far:
            count = 1
            max_so_far = node.val

        count += self.countGoodNodes(node.left, max_so_far)
        count += self.countGoodNodes(node.right, max_so_far)

        return count
