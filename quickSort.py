# 快速排序
# 原地修改
# 选择一个数，按照某种规律归位：位置左边的数都小于它，位置边的数都大于他，递归完成所有
# 时间复杂度 O(nlog(n))

import random


def get_index(li, left, right):

    tmp = li[left]

    while left < right:

        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] < tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if right > left:
        idx = get_index(li, left, right)
        _quick_sort(li, left, idx - 1)
        _quick_sort(li, idx + 1, right)


def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    quick_sort(li)
    print(li)
