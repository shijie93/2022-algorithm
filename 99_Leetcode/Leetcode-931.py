from typing import List


class Solution:
    """给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
"""
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        height = len(matrix)
        width = len(matrix[0])
        
        memo = [[66666] * width for _ in range(height)]
        
        def dp(matrix, i, j):
            if i >= height or i < 0 or j >= width or j < 0:
                return float('inf')
            
            # base case
            if i == 0:
                return matrix[i][j]

            # 备忘录 1
            if memo[i][j] != 66666:
                return memo[i][j]

            # 备忘录 2
            memo[i][j] = matrix[i][j] + min(
                dp(matrix, i - 1, j - 1),
                dp(matrix, i - 1, j),
                dp(matrix, i - 1, j + 1)
            )

            return memo[i][j]

        res = float('inf')
        for j in range(width):
            res = min(res, dp(matrix, height - 1, j))

        return res
        