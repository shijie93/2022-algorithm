class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return None
        return self.generate(1, n)

    def generate(self, left, right):
        trees = list()
        if left > right: 
            trees.append(None)
            return trees

        for i in range(left, right +1):
            leftTrees = self.generate(left, i - 1)
            rightTrees = self.generate(i+1, right)

            for l in leftTrees:
                for r in rightTrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)
        
        return trees