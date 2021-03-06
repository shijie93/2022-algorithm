# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(0, len(nums) - 1, nums)

    def construct(self, left, right, nums):

            if left > right:
                return None
            
            maxv = -1
            index = -1
            for i, val in enumerate(nums[left:right+1]):
                if val > maxv:
                    maxv = val
                    index = i + left
                
                    
            p = TreeNode(maxv)

            p.left = self.construct(left, index-1, nums)
            p.right = self.construct(index + 1, right, nums)

            return p