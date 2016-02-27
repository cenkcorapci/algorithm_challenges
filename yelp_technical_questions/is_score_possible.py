numbers = [3, 7, 12]
known_results = {}


def check(numbers_list, goal, depth, max_depth):
    if max_depth <= depth:
        return False
    if goal in numbers_list:
        known_results[goal] = True
        return True
    elif goal in known_results:
        return known_results[goal]
    else:
        for i in numbers_list:
            r = goal - i
            if r == 0:
                return True
            elif r < 0:
                continue
            elif r > 0:
                check(numbers_list, r, depth + 1, max_depth)
    return False


# total = int(raw_input().strip())

for total in xrange(9, 30):
    filtered = [x for x in numbers if x <= total]
    if len(filtered) > 0:
        m = min(filtered)
        max_depth = total / m + 1 if m != 0 else total
        print total, " : ", check(numbers, total, 0, max_depth)
