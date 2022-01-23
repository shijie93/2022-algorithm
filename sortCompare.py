from json.tool import main
import random
import copy
from bubbleSort import bubble_sort
from calTime import cal_avg_time
from heapSort import heaq_sort, use_heapq_sort
from insertSort import insert_sort
from quickSort import quick_sort
from selectionSort import selection_sort

count = 2000

li1 = random.sample(range(1, 10000), count)
li2 = random.sample(range(1, 10000), count)
li3 = random.sample(range(1, 10000), count)
li4 = random.sample(range(1, 10000), count)
li5 = random.sample(range(1, 10000), count)


@cal_avg_time(times=5)
def test_sorted(f):
    c_li1 = copy.deepcopy(li1)
    c_li2 = copy.deepcopy(li2)
    c_li3 = copy.deepcopy(li3)
    c_li4 = copy.deepcopy(li4)
    c_li5 = copy.deepcopy(li5)

    f(c_li1)
    f(c_li2)
    f(c_li3)
    f(c_li4)
    f(c_li5)
    return c_li1, c_li2, c_li3, c_li4, c_li5


if __name__ == '__main__':
    tmp = test_sorted(bubble_sort)
    assert tmp == test_sorted(insert_sort)
    assert tmp == test_sorted(selection_sort)
    assert tmp == test_sorted(quick_sort)
    assert tmp == test_sorted(heaq_sort)
    assert tmp == test_sorted(use_heapq_sort)
