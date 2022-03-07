class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        输入：n = 3
        输出：[[1,2,3],[8,9,4],[7,6,5]]
        '''

        # 顺序为右，下，左，上
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tmp = [[0] * n for _ in range(n)]
        res = [[0] * n for _ in range(n)]
        i = j = 0
        tmp[0][0] = 1
        pre = steps[0]
        num = 0
        while i < n and j < n:
            num += 1
            res[i][j] = num
            for step in [pre] + steps:
                if 0 <= i+step[0] < n and 0 <= j+step[1] < n and tmp[i+step[0]][j+step[1]] == 0:
                    tmp[i+step[0]][j+step[1]] = 1
                    i += step[0]
                    j += step[1]
                    pre = step
                    break
            else:
                break
        return res