possibilities = set()


def get_all(a, b):
    if len(b) == 0:
        possibilities.add(a)
        return
    i = 0
    c = str(b)[i]
    while not c.isalpha():
        a += c
        i += 1
        c = b[i]

    get_all(a + c.lower(), b[i + 1:])
    get_all(a + c.upper(), b[i + 1:])


get_all("", raw_input().strip())
print possibilities
