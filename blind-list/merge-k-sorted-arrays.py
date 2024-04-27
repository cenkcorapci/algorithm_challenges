from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        while a and b:
            if a.val < b.val:
                temp.next = a
                temp = temp.next
                a = a.next
            else:
                temp.next = b
                temp = temp.next
                b = b.next
        while a:
            temp.next = a
            temp = temp.next
            a = a.next
        while b:
            temp.next = b
            temp = temp.next
            b = b.next
        return dummy.next

    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)
