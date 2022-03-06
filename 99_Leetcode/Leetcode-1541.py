class Solution:
    def minInsertions(self, s: str) -> int:
        res = need = 0

        for c in s:
            # 如果是左括号
            if c == '(':
                # 对于右括号的需求量加2
                need += 2

                # 若对右括号的需求量为奇数，需要插⼊ 1 个右括号
                if need % 2 == 1:
                    res += 1
                    need -= 1

            # 如果是右括号
            if c == ')':
                # 对于右括号的需求量减去1
                need -= 1

                # 如果右括号的需求量负数，右括号太多了
                if need == -1:
                    # 插入一个左括号
                    res += 1
                    # 右括号的需求量改为1，2 - 1
                    need = 1

        return res + need