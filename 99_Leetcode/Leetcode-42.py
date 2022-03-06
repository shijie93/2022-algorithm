class Solution:
    def trap(self, height: List[int]) -> int:

        # 预处理得出每个位置leftmax和rightmax
        leftMax = [0] * (len(height))
        maxv = -1
        for i in range(0, len(height)):
            maxv = max(maxv, height[i])
            leftMax[i] = maxv
        
        rightMax = [0] * (len(height))
        maxv = -1
        for i in range(len(height) - 1, -1, -1):
            maxv = max(maxv, height[i])
            rightMax[i] = maxv
        
        total = 0
        for i in range(len(height)):
            add = min(leftMax[i], rightMax[i]) - height[i]
            print(add)
            total += add

        return total