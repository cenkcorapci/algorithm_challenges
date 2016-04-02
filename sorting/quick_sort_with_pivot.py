from random import randint


def qsort(list):
    if not list:
        return []
    else:
        wall = 0
        while wall < len(list):
            pivot = list[-1]
            for i in range(wall, len(list)):
                if list[i] < pivot:
                    list[wall], list[i] = list[i], list[wall]
                    wall += 1
            list[wall], list[-1] = list[-1], list[wall]
            wall += 1
    return list


a_set = set([randint(0, 10) for i in xrange(10)])
print(qsort(list(a_set)))
