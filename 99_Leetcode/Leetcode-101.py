# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        def check(left, right):
            if not left and not right: return True
            if left and not right: return False
            if right and not left: return False

            if left.val == right.val:
                return True
            
            return check(left.left, left.right) and check(right.left, right.right)
        
        return check(root.left, root.right)