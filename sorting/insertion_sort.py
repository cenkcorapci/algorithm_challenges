from random import randint


def insertion_sort(l):
    for i, key in enumerate(l[1:]):
        j = i - 1
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


aset = set([randint(0, 10) for i in xrange(10)])
print(insertion_sort(list(aset)))
