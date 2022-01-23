

import copy
import random
import heapq


def sift(li, low, high):
    # 向下调整大顶堆
    tmp = li[low]
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1

        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def heaq_sort(li):
    # 构建大顶堆
    for i in range((len(li) - 1) // 2, -1, -1):
        sift(li, i, len(li) - 1)

    # 原地排序
    for i in range((len(li)-1), 0, -1):
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i - 1)


def use_heapq_sort(li):
    tmp = copy.deepcopy(li)
    heapq.heapify(tmp)

    count = 0
    while len(tmp) > 0:
        li[count] = heapq.heappop(tmp)
        count += 1


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    li1 = copy.deepcopy(li)
    heaq_sort(li1)
    print(li1)

    li2 = copy.deepcopy(li)
    use_heapq_sort(li2)
    print(li2)
