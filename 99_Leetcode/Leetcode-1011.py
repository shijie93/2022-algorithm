
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。
        传送带上的第 i 个包裹的重量为 weights[i]。每一天  我们都会按给出重量 weights 的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
        返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
        输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        输出：15
        '''
        def f(weights, x):
            days = 0
            w = 0
            for v in weights:
                if v > x: # 无法运载，返回上限天
                    return int(3e7)

                if (w == 0 and v < x) or w + v > x:
                    days += 1
                    w = v
                elif w + v == x:
                    w = 0
                else:
                    w += v
                    
            return days
        
        left = 1
        right = int(3e7)

        while left <= right:

            mid = left + (right - left) // 2

            ret = f(weights, mid)
            if ret < days:
                right = mid - 1
            elif ret > days:
                left = mid + 1
            elif ret == days:
                right = mid - 1
        
        return left
        