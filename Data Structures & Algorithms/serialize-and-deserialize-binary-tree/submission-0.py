# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def recserialize(self, root: TreeNode, string: str) -> str:
        if root is None:
            string += "null,"
        else:
            string += str(root.val) + ","
            string = self.recserialize(root.left, string)
            string = self.recserialize(root.right, string)

        return string

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.recserialize(root, "")
        
    def recdeserialize(self, strs: List[str]) -> TreeNode:
        if strs[0] == "null":
            strs.pop(0)
            return None
        
        root = TreeNode(int(strs[0]))
        strs.pop(0)
        root.left = self.recdeserialize(strs)
        root.right = self.recdeserialize(strs)

        return root

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        str_list = data.split(",")
        return self.recdeserialize(str_list)




