# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = self.inOrder(root, [])
        return nums[k-1]
        
    def inOrder(self, root: TreeNode, arr: List[int]) -> List[int]:
        if root is None:
            return arr
        
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr
