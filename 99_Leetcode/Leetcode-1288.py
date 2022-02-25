class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
            输入：intervals = [[1,4],[3,6],[2,8]]
            输出：2
            解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
        '''

        # 将数组start 升序排列，如果 start 相同，则降序

        intervals.sort(key=lambda a: (a[0], -a[1]))

        res = 0
        left = intervals[0][0]
        right = intervals[0][1]

        for i in range(1, len(intervals)):
            inter = intervals[i]

            # 重叠
            if left <= inter[0] and right >= inter[1]:
                res += 1

            # 交集，扩大右
            elif right >= inter[0] and right <= inter[1]:
                right = inter[1]
            
            # 不相交，更新指针
            else:
                left = inter[0]
                right = inter[1]

        return len(intervals) - res
