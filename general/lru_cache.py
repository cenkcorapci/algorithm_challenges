from circular_doubly_linked_list import CircularDoublyLinkedList, Node


class LRUCache(object):
    def __init__(self, maxsize=5):
        self.cache_list = CircularDoublyLinkedList()
        self.cache_table = {}
        self.misses = 0
        self.hits = 0
        self.requests = 0
        self.maxsize = maxsize

    def get_size(self):

        if self.cache_list.root == None:
            return 0
        else:
            i = 1
            item = self.cache_list.root.next
            while item != self.cache_list.root:
                i += 1
                item = item.next
            return i

    def save_and_return(self, func, *args, **kwargs):
        key = self.make_hashed_func_object(func, *args, **kwargs)
        if self.cache_table.get(key, None) != None:
            # already in cache
            desired_node = self.cache_table[key]
            self.hits += 1
        else:
            # not in cache
            desired_node = Node(func(*args, **kwargs))
            self.cache_table[key] = desired_node
            self.misses += 1
            if self.is_full():
                self.delete_oldest()
        self.mark_most_recent(desired_node)
        return desired_node.value

    def delete_oldest(self):
        oldest = self.cache_list.root.previous
        oldest.previous.next = self.cache_list.root
        self.cache_list.root.previous = oldest.previous
        oldest = None

    def is_full(self):
        if self.get_size() >= self.maxsize:
            return True
        return False

    def mark_most_recent(self, recent_node):
        if self.cache_list.root == None:
            # list is empty
            recent_node.previous = recent_node.next = recent_node
            self.cache_list.root = recent_node
        elif recent_node.next != None and recent_node.previous != None:
            # node is already in list somewhere
            self.remove_from_middle(recent_node)
            self.add_to_head(recent_node)
        else:
            # node not in list
            self.add_to_head(recent_node)

    def add_to_head(self, new_root):
        old_root = self.cache_list.root
        tail = old_root.previous
        tail.next = new_root
        new_root.previous = tail
        old_root.previous = new_root
        new_root.next = old_root
        self.cache_list.root = new_root

    def remove_from_middle(self, new_root):
        new_root.next.previous = new_root.previous
        new_root.previous.next = new_root.next

    def make_hashed_func_object(self, func, *args, **kwargs):
        return hash(repr([func, args, kwargs]))

    def get_first(self):
        return self.cache_list.root

    def get_last(self):
        return self.cache_list.root.previous

    def get_cache_list(self):
        l = []
        item = self.cache_list.root
        if item == None:
            return []
        while item.next != self.cache_list.root:
            l.append(item.value)
            item = item.next
        l.append(item.value)
        return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # doctest.run_docstring_examples(LRUCache.make_hashed_func_object, globals())
