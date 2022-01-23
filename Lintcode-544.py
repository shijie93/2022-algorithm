# 在一个数组中找到前K大的数
import random

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    @staticmethod
    def sift(li, low, high):
        # 向下调整小顶堆
        tmp = li[low]
        i = low
        j = 2 * i + 1

        while j <= high:
            if j + 1 <= high and li[j + 1] < li[j]:
                j = j + 1

            if li[j] < tmp:
                li[i] = li[j]
                i = j
                j = 2 * i + 1
            else:
                break
        li[i] = tmp


    def topk(self, nums, k):
        heap = nums[0:k]

        # 使用前k个数构建小顶堆
        for i in range((k - 2) // 2, -1, -1):
            self.sift(heap, i, k - 1)

        # 遍历
        for i in range(k, len(nums) - 1):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.sift(heap, 0, k - 1)

        for i in range(k-1, -1 -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.sift(heap, 0, i - 1)

        return heap

if __name__ == '__main__':
    li = list(range(0, 20))
    random.shuffle(li)
    s = Solution()
    print(s.topk(li, 10))
