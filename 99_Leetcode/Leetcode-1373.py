class Solution:

    def __init__(self) -> None:
        self.maxv = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ## 通过后序遍历，返回一个4位的数组
        ## 数组的第一位为是否为 BST
        ## 数组的第二位为树的节点最小值
        ## 数组的第三位为树的节点最大值
        ## 数组的第四位为树的节点数值和
        self.check(root)
        return self.maxv
    
    def check(self, root):
        if not root:
            return [1, 5e4, -5e4, 0]
        
        left = self.check(root.left)
        right = self.check(root.right)
        ret = [0 for _ in range(4)]

        if left[0] == 1 and right[0] ==1 and root.val > left[2] and root.val < right[1]:
            ret[0] = 1
            ret[1] = min(left[1], root.val)
            ret[2] = max(right[2], root.val)
            ret[3] = left[3] + right[3] + root.val
            self.maxv = max(self.maxv, ret[3])
        else:
            ret[0] = 0
        
        return ret