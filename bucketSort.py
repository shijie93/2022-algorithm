import random

def bucket_sort(li, n=100, max=10000):
    buckets = [[] for _ in range(0, n)]

    for val in li:
        bin_index = min(val // (max // n), n-1)
        buckets[bin_index].append(val)
        for i in range(len(buckets[bin_index]) - 2, -1, -1):
            if buckets[bin_index][i] > buckets[bin_index][i + 1]:
                buckets[bin_index][i + 1], buckets[bin_index][i] = buckets[bin_index][i], buckets[bin_index][i+1]
            else:
                break
    ret = []
    for bucket in buckets:
        ret.extend(bucket)

    li[:] = ret


if __name__ == '__main__':
    li = random.sample(range(1, 20), 10)
    print(li)
    bucket_sort(li)
    print(li)