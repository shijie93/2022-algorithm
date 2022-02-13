# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        
        # 找到根节点值
        rootVal = preorder[preStart]

        # 在中序中找到最大值的下标
        index = -1
        for i, v in enumerate(inorder[inStart:inEnd+1]):
            if v == rootVal:
                index = i + inStart
                break

        root = TreeNode(rootVal)

        # 左子树长度
        leftSize = index - inStart
        root.left = self.build(preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, preEnd)

        return root