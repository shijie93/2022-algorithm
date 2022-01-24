# 计数排序
# 用空间换时间

import random

def count_sort(li, max_v=100000):
    cache = [0 for _ in range(max_v + 1)]

    for i in li:
        cache[i] += 1
    
    ret = []
    for index, val in enumerate(cache):
        for i in range(val):
            ret.append(index)
    
    li[:] = ret


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    print(li)
    count_sort(li, 20)
    print(li)
