class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        # 基本思路
        # 从后往前，如果 S遇到#，skips += 1, 如果不是，判断 skips，如果大于0则自减少，继续迭代，如果skips等于0，则此时无法忽略，
        # 转向 T ，思路与 S 相同，无法忽略时则比较，一旦遇到不匹配的则退出，遍历完都没有推出则表示成功
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    # backspace
                    skipS -= 1
                    i -= 1
                else:
                    # 停下等待比较
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    # backspace
                    skipT -= 1
                    j -= 1
                else:
                    # 停下等待比较
                    break
            # 如果上面两个循环是因为待比较而不是循环耗尽而退出，则需要比较
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            # 表示某一个循环耗尽，此时也一定无法比较
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True
