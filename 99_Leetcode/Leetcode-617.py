class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged