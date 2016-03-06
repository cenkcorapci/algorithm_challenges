t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    nums = [int(x) for x in raw_input().split()]
    if n % 2 == 0:
        print 0
    else:
        result = 0
        for j in xrange(n):
            if (j + 1) % 2 == 1:
                result = result ^ nums[j]
        print result
