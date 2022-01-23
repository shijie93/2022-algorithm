# 二分查找
# 前置条件：列表有序
# 分配两个“指针”指向列表的首尾，将列表一分为二，根据待查找元素与指针中间数的关系，选择查找不同的部分，
# 时间复杂度：O(logN)
from calTime import cal_time

@cal_time
def bin_search(li, val):
    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return


print(bin_search([1,4,6,8,9,12,34], 0))