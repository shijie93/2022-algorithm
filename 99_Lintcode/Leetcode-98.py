# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def f(root, minv, maxv):
            if not root: return True
            if root.val <= minv: return False
            if root.val >= maxv: return False

            return f(root.left, minv, root.val) and f(root.right, root.val, maxv)
        return f(root, float('-inf'), float('inf'))
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.max = float('inf')
        self.res = True
        def f(root):
            if not root or not self.res:
                return
            
            f(root.right)
            if root.val < self.max:
                self.max = root.val
            else:
                self.res = False
                return
            f(root.left)

        f(root)
        return self.res
"""
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.res = True
        
        def f(root):
            if not root:
                return float('inf'), float('-inf')

            min1, max1 = f(root.left)
            min2, max2 = f(root.right)

            if root.val > max1 and root.val < min2:
                return min(min1, root.val), max(max2, root.val)
            else:
                self.res = False
            return float('inf'), float('-inf')
        
        f(root)
        return self.res

"""