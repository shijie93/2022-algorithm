# 归并排序

import random


def merge(li, low, mid, high):
    left = low
    right = mid + 1

    ret = []
    while left <= mid and right <= high:
        if li[left] < li[right]:
            ret.append(li[left])
            left += 1
        else:
            ret.append(li[right])
            right += 1

    while left <= mid:
        ret.append(li[left])
        left += 1
    
    while right <= high:
        ret.append(li[right])
        right += 1
    
    li[low:high+1] = ret


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


def merge_sort(li):
    _merge_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    print(li, len(li))
    merge_sort(li)
    print(li, len(li))
