class MinHeap():
    def __init__(self):
        self.height = 0
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        self._heapifiy_from(len(self.heap) - 1)

    def remove(self, item):
        i = 0
        while i < len(self.heap):
            if item == self.heap[i]:
                break
        if i == len(self.heap):
            return

        while i < len(self.heap):
            right = self._right_index(i)
            left = self._left_index(i)
            if right == None and left == None:
                del self.heap[i]
                break
            elif right != None and left == None:
                self.heap[i] = self.heap[right]
                i = right
            elif right == None and left != None:
                self.heap[i] = self.heap[left]
                i = left
            elif right != None and left != None:
                if self.heap[right] > self.heap[left]:
                    self.heap[i] = self.heap[right]
                    i = right
                elif self.heap[right] <= self.heap[left]:
                    self.heap[i] = self.heap[left]
                    i = left

    def _heapifiy_from(self, i):
        i = len(self.heap) - 1
        while i > 0:
            parent = self._parent_index(i)
            if parent != None and self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _left_index(self, i):
        indx = 2 * i + 1
        return indx if indx > len(self.heap) else None

    def _left(self, i):
        indx = self._left_index(i)
        return self.heap[indx] if indx != None else None

    def _right_index(self, i):
        indx = 2 * i + 2
        return indx if indx > len(self.heap) else None

    def _right(self, i):
        indx = self._right_index(i)
        return self.heap[indx] if indx != None else None

    def _parent_index(self, i):
        return (i - 1) / 2 if i >= 1 else None

    def _parent(self, i):
        indx = self._parent_index(i)
        return self.heap[indx] if indx != None else None

    def get_min(self):
        return self.heap[0] if 0 < len(self.heap) else None


commands_count = int(raw_input().strip())
heap = MinHeap()
for i in xrange(0, commands_count):
    cmd = raw_input().strip().split(" ")
    if cmd[0] == "1":
        heap.add(int(cmd[1]))
    if cmd[0] == "2":
        heap.remove(int(cmd[1]))
    if cmd[0] == "3":
        print heap.get_min()
