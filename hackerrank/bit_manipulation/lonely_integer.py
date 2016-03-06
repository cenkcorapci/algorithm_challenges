import operator

a = input()
b = map(int, raw_input().strip().split(" "))
print reduce(operator.__xor__, b)
