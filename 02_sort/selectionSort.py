# 选择排序
# 原地修改
# 将列表分为有序区和无序区，有序区在前，每次一次比较无序区，将最大(或最小)的值放置在无序区的第一个位置，无序区从后一个开始重复步骤
# 时间复杂度 O(n^2)
import random

def selection_sort(li):
    for i in range(0, len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j

        if min_index > i:
            li[min_index], li[i] = li[i], li[min_index]

if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    selection_sort(li)
    print(li)
