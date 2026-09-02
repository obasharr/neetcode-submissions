# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parentval = root.val
        pval = p.val
        qval = q.val

        if pval > parentval and qval > parentval:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if pval < parentval and qval < parentval:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root