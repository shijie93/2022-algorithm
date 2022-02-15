# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder,0, len(inorder) - 1, postorder, 0 , len(postorder) - 1)


    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if postStart > postEnd or inStart > inEnd:
            return None
        
        # 找到根节点值
        rootVal = postorder[postEnd]

        # 在中序中找到最大值的下标
        index = -1
        for i, v in enumerate(inorder[inStart:inEnd+1]):
            if v == rootVal:
                index = i + inStart
                break

        root = TreeNode(rootVal)

        # 左子树长度
        leftSize = index - inStart
        root.left = self.build(inorder, inStart, index - 1, postorder, postStart, postStart + leftSize - 1)
        root.right = self.build(inorder, index + 1, inEnd, postorder, postStart + leftSize, postEnd - 1)

        return root