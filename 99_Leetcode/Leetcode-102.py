# Definition for a binary tree node.
from typing import List

from torch import le

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """dfs"""
        self.result = []

        def dfs(root, level):
            if not root: return None

            if len(self.result) < level + 1:
                self.result.append([])
            
            self.result[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return self.result

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         """BFS"""
#         if not root: return []

#         res = []
#         queue = collections.deque()
#         queue.append(root)

#         while queue:
#             level_size = len(queue)
#             current_level = []

#             for i in range(level_size):
#                 node = queue.popleft()
#                 current_level.append(node.val)

#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
            
#             res.append(current_level)
#         return res