# 汉诺塔问题
# 汉诺塔问题，是心理学实验研究常用的任务之一。
# 该问题的主要材料包括三根高度相同的柱子和一些大小及颜色不同的圆盘，三根柱子分别为起始柱A、辅助柱B及目标柱C。
# 开始圆盘在A上，圆盘从上至下一次从小到大，问题是从将圆盘从A移动到C上，要求一次只能移动一个，且大圆盘不能放置在小圆盘上

# 解题思路:
# 通过递归，将问题分解为一个小问题：
# 假定现在A上有2个圆盘，则步骤为将 a->b a->c b->c
from calTime import cal_time


def _hanoi(n, a, b, c):

    if n > 0:
        _hanoi(n-1, a, c, b)  # a -> b
        print(f"{a} -> {c}")  # a -> c
        _hanoi(n-1, b, a, c)  # b -> c


@cal_time
def hanoi(n, a, b, c):
    _hanoi(n, a, b, c)


hanoi(3, "A", "B", "C")