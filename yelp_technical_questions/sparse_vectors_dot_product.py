a_map = {}
b_map = {}

a, b = [int(x) for x in raw_input().strip().split(" ")]

size = 0

for i in xrange(0, a):
    x, y = [int(x.strip()) for x in raw_input().strip().split(" ")]
    if x > size:
        size = x
    a_map[x] = y

for i in xrange(0, b):
    x, y = [int(x.strip()) for x in raw_input().strip().split(" ")]
    if x > size:
        size = x
    b_map[x] = y

dot_product = 0
for pos in xrange(0, size + 1):
    if pos in a_map and pos in b_map:
        dot_product += a_map[pos] * b_map[pos]

print dot_product
