import math
import operator

_l = int(raw_input())

_r = int(raw_input())

res = 2 ** (math.floor(math.log(operator.__xor__(_l, _r), 2)) + 1) - 1
print(int(res))
