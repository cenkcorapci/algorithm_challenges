from random import randint


def counting_sort(a, min, max):
    cnt = [0] * (max - min + 1)
    for x in a:
        cnt[x - min] += 1

    return [x for x, n in enumerate(cnt, start=min)
            for i in xrange(n)]


l = list(set([randint(0, 100) for i in xrange(20)]))
print(counting_sort(l, min(l), max(l)))
