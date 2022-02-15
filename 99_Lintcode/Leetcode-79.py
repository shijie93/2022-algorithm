from typing import List
import collections


class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return []
        if word == "":
            return []

        self.ret = False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if len(word) == 1:
                        return True
                    self._dfs(board, 0, x, y, word)
        return self.ret

    def _dfs(self, board, level, x, y, word: str):
        if level == len(word):
            self.ret = True
            return self.ret

        if word[level] != board[x][y]:
            return False

        tmp, board[x][y] = board[x][y], '@'
        for i in range(4):
            n_x, n_y = x + self.dx[i], y + self.dy[i]
            if 0 <= n_x < len(board) and 0 <= n_y < len(board[0]):
                if board[n_x][n_y] != '@':
                    self._dfs(board, level + 1, n_x, n_y, word)
        board[x][y] = tmp

        if len(word) == level + 1:
            self.ret = True
            return self.ret
