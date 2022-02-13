class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.result = 1e4
        def dfs(root, level):
            if not root: return
            if root.left: dfs(root.left, level +1)
            if root.right: dfs(root.right, level +1)
            if not root.left and not root.right:
                self.result = min(self.result, level)

        dfs(root, 1)
        return self.result