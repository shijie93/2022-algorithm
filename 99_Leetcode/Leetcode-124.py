# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = -1000 - 1
        def traverse(root):
            if not root: return 0

            L = max(0, traverse(root.left))
            R = max(0, traverse(root.right))

            self.res = max(self.res, L + R + root.val)
            return max(L, R) + root.val

        traverse(root)
        return self.res