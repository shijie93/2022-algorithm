# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = collections.defaultdict(collections.deque)
        def traverse(root, level):
            if not root: return
            
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        traverse(root, 0)

        return [list(res[i]) for i in res]