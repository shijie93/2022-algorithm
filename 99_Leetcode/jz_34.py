# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = list()
        path = list()
        
        def dfs(root: TreeNode, target: int):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                ret.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        
        dfs(root, target)
        return ret
