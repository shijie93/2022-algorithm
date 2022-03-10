from re import I


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        输入:nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        输出:[1,2,2,3,5,6]
        解释:需要合并 [1,2,3] 和 [2,5,6] 。
        合并结果是 [1,2,2,3,5,6] ,其中斜体加粗标注的为 nums1 中的元素。
        """

        cur = 0
        while cur < m:
            nums1[m + cur] = nums1[cur]
            cur += 1
        
        print(nums1)


if __name__ == '__main__':
    s = Solution()

    assert s.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]