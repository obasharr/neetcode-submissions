# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.maxGain(root)
        return self.maxSum

    def maxGain(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        leftGain = max(self.maxGain(root.left), 0)
        rightGain = max(self.maxGain(root.right), 0)

        priceNewPath = root.val + leftGain + rightGain

        self.maxSum = max(self.maxSum, priceNewPath)

        return root.val + max(leftGain, rightGain)

        