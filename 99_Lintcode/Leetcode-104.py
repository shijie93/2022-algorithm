class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root, level):
            if not root: return
            if root.left: dfs(root.left, level +1)
            if root.right: dfs(root.right, level +1)
            self.result = max(self.result, level)

        dfs(root, 1)
        return self.result