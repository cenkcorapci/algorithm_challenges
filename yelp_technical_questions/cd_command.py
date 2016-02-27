class PathStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_path(self):
        d = ""
        for folder in self.items:
            d += "/" + folder
        return d

def cd(curr, ops):

    s = PathStack()
    for c in str(curr).strip().split("/"):
        if c != "":
            s.push(c)

    for op in str(ops).strip().split("/"):
        if op == "..":
            s.pop()
        else:
            s.push(op)
    return s.get_path()


curr, ops = raw_input().split(",")
print cd(curr, ops)
# example input a/b,c/../d/e/../f
