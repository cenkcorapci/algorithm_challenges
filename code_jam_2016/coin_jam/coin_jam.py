def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def prime_check(num):
    a = 2
    step = num - 1
    while num > a:
        if step % a == 0:
            return False
        a += 1

    return True


num_test_cases = int(raw_input().strip(" "))


def min_flips(order):
    pre = 'n'
    flips = 0
    for c in order:
        if pre == 'n':
            pre = c
            continue
        if c != pre:
            pre = c
            flips += 1

    if pre == '-':
        flips += 1
    return flips


for case in xrange(1, num_test_cases + 1):
    print "Case #%d: %d" % (case, min_flips(raw_input().strip(" ")))
