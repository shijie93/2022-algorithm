# 冒泡排序
# 每一轮从前往后两两比较，根据大小调换位置，每一轮过后无序区最大(或最小)的元素会想水中的泡泡一样上浮
# 时间复杂度 O(n^2)

import random

def bubble_sort(li):
    for i in range(0, len(li)):
        is_change = False
        for j in range(0, len(li) - i - 1):
            if li[j+1] < li[j]:
                li[j+1], li[j] = li[j], li[j+1]
                is_change = True
        if not is_change:
            return

if __name__ == '__main__':
    li = random.sample(range(1, 400000), 5000)
    bubble_sort(li)
    # print(li)
