# 线性查找也称为顺序查找
# 指按顺序查找元素
# 时间复杂度 O(N)
def linear_search(li, val):
    for idx, v in enumerate(li):
        if v == val:
            return idx
    return


print(linear_search([1, 2, 3, 4, 5, 6, 7], 3))
