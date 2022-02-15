# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 由于是 BST，所以可以根据数值关系决定去左子树还是右子树中进行查找
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        
        # 说明q和p分别在左右子树中，当前节点为公共祖先
        return root