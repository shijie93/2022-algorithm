import random

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        for j in range(i - 1, -1, -gap):
            if j + gap < len(li) and li[j] > li[j + gap]:
                li[j], li[j + gap] = li[j + gap], li[j]
            else: # important
                break


def shell_sort(li):
    d = len(li) // 2

    while d >= 1:
        insert_sort_gap(li, d)

        d //= 2


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    print(li)
    shell_sort(li)
    print(li)
