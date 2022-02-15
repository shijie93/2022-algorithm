# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ','
    NULL = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return self.NULL
        
        subLeft = self.serialize(root.left)
        subRight = self.serialize(root.right)

        sub = subLeft + self.SEP + subRight + self.SEP + str(root.val)
        return sub
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataList = data.split(self.SEP)
        def f(data):
            if not data:
                return None
            
            rootval = data.pop()
            if rootval == self.NULL:
                return None
            root = TreeNode(rootval)

            # 由于后续遍历，要先递归右子树
            root.right = f(data)
            root.left = f(data)
            return root
        
        return f(dataList)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))