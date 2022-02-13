# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """从大到小降序打印 BST 节点的值，维护一个外部累加变量sum，然后把sum赋值给 BST 中的每一个节点，BST 转化成累加树"""
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self.build(root)
        return root

    def build(self, root):
        if not root: return None
        self.build(root.right)
        self.sum += root.val
        root.val = self.sum
        self.build(root.left)