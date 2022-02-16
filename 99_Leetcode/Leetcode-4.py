from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)

        def getKth(k):
            
            p1 = p2 = 0

            while True:
            
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                    k -= 1
                elif nums1[p1] > nums2[p2]:
                    p2 += 1
                    k -= 1
                else:
                    if p1 < l1:
                        p1 += 1
                        k -= 1
                    if p2 < l2:
                        p2 += 1
                        k -= 1
                
                if p1 == l1:
                    p1 -= 1
                if p2 == l2:
                    p2 -= 1

                if k == -1:
                    return min(nums1[p1], nums2[p2])

        
        total = l1 + l2
        if total & 1 == 1:
            return getKth(total // 2 + 1)
        else:
            return (getKth(total // 2) + getKth(total // 2 + 1)) / 2

