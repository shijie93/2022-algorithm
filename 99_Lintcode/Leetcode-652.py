# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:

    def __init__(self):
        self.res = []
        self.dup = defaultdict(int)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.find(root)
        return self.res

    def find(self, root):

        if not root:
            return '#'
        
        leftstring = self.find(root.left)
        rightstring = self.find(root.right)

        substring = leftstring + ',' + rightstring + ',' + str(root.val)

        if self.dup[substring] == 1:
            self.res.append(root)
        
        self.dup[substring] += 1
        return substring
