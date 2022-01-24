# 插入排序
# 原地修改
# 将列表分为有序区和无序区，有序区在前，每次从无序区中取出一个插入有序区
# 时间复杂度 O(n^2)
import random


def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i - 1, -1, -1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    insert_sort(li)
    print(li)
