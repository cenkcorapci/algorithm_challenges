arr = [int(x) for x in raw_input().strip().split(" ")]

sum_of_all = sum(arr)
left_sum = 0
indexes = []
for i, a in enumerate(arr):
    if left_sum * 2 == (sum_of_all - a):
        indexes.append(i)
    left_sum += a
print indexes
#inp -7 1 5 2 -4 3 0
# 9 8 7 2 7 3 7 4 1 4 0