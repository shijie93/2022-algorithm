from typing import List
import collections

class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0 , 0, -1, 1]

    END_OF_WORD = '#'
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return []
        self.res = set()
        
        # 构建由字典组成的前缀树，将单次存入前缀树中。
        root = collections.defaultdict()
        for word in words:
            cur = root
            for c in word:
                cur = cur.setdefault(c, collections.defaultdict())
            cur[self.END_OF_WORD] = self.END_OF_WORD

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in root:
                    self._dfs(board, x, y, "", root)
        return list(self.res)

    def _dfs(self, board, x, y, curWord, dictWords):
        curWord += board[x][y]
        dictWords = dictWords[board[x][y]]

        if self.END_OF_WORD in dictWords:
            self.res.add(curWord)
        
        tmp, board[x][y] = board[x][y], '@'
        for i in range(4):
            n_x, n_y =  x + self.dx[i], y + self.dy[i]
            if 0 <= n_x < len(board) and 0 <= n_y < len(board[0]):
                if board[n_x][n_y] != '@' and board[n_x][n_y] in dictWords:
                    self._dfs(board, n_x, n_y, curWord, dictWords)
        board[x][y] = tmp