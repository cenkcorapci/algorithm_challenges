import math


def solution(predicted, observed):
    total = 0
    n = len(predicted)
    for p, o in zip(predicted, observed):
        total += math.pow(p - o, 2) / n
    return math.sqrt(total)

