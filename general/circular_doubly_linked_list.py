class Node(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CircularDoublyLinkedList(object):
    """
    Implements a double, circular linked list
    """

    def __init__(self, value=None):
        if value == None:
            self.root = None
        else:
            self.root = Node(value)
            self.root.prev = self.root
            self.root.next = self.root

    def get_first(self):
        return self.root

    def get_last(self):
        return self.root.prev

    def insert_at_beginning(self, value):

        new = Node(value)
        if self.root == None:
            self.root = new
        new.next = self.root
        new.prev = self.root.prev
        self.root.prev.next = new
        self.root.prev = new
        self.root = new

    def insert_at_end(self, value):

        new = Node(value)
        if self.root == None:
            self.root = new
        last = self.root.prev
        last.next = new
        new.prev = last
        new.next = self.root
        self.root.prev = new

    def remove_from_beginning(self):

        new_root = self.root.next
        new_root.prev = self.root.prev
        self.root.prev.next = new_root
        self.root = new_root

    def remove_from_end(self):

        self.get_last().prev.next = self.root
        self.root.prev = self.get_last().prev

    def size(self):
        if self.root == None:
            # list is empty
            return 0
        else:
            item = self.root
            i = 1
            while item.next != self.root:
                i += 1
                item = item.next
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
