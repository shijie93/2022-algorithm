from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # count[i] = count[i & (i - 1)] + 1

        counts = dict()
        counts[0] = 0
        for i in range(1, n + 1):
            counts[i] = counts[i & (i-1)] + 1

        return list(counts.values())
