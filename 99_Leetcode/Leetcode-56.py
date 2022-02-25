class Solution:
    '''
    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/merge-intervals
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 按照 start 升序
        intervals.sort(key=lambda a: a[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):

            cur = intervals[i]

            last = res[-1]

            if cur[0] > last[1]:
                res.append(cur)
            else:
                last[1] = max(last[1], cur[1])
        return res