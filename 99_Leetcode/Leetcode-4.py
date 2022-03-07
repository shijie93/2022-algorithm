from tkinter import N


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        total = m + n
        if total % 2 == 0:
            # 偶数
            return (self.getk(nums1, nums2, total // 2 - 1) + self.getk(nums1, nums2, total // 2)) / 2
        else:
            # 奇数
            return self.getk(nums1, nums2, total // 2)

    def getk(self, nums1, nums2, k):
        # k 从 0 开始
        l1 = l2 = 0
        m = len(nums1)
        n = len(nums2)
        res = None
        while l1 < m and l2 < n:
            if nums1[l1] < nums2[l2]:
                k -= 1
                l1 += 1
                if k == -1:
                    return nums1[l1-1]
            else:
                k -= 1
                l2 += 1
                if k == -1:
                    return nums2[l2-1]
        
        if l1 < m:
            return nums1[l1 + k]
        
        if l2 < n:
            return nums2[l2 + k]