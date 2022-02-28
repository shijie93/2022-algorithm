class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height) - 1, 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            left, right = (left + 1, right) if height[left] < height[right] else (left, right - 1)
        return res