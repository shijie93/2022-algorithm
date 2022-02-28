import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。'''

        n = len(matrix)
        m = len(matrix[0])

        # 顺序为右，下，左，上
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tmp = np.zeros((n, m), dtype='int8')
        res = []
        i = j = 0
        tmp[0][0] = 1
        pre = steps[0]
        while i < n and j < m:
            res.append(matrix[i][j])
            for step in [pre] + steps:
                if 0 <= i+step[0] < n and 0 <= j+step[1] < m and tmp[i+step[0]][j+step[1]] == 0:
                    tmp[i+step[0]][j+step[1]] = 1
                    i += step[0]
                    j += step[1]
                    pre = step
                    break
            else:
                break
        return res