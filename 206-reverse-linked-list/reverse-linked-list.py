# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        if head is None:
            return None
        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1
        tail = curr
        temp = head
        head = tail
        tail = temp
        after = temp.next
        before = None
        for _ in range(length+1):
            after = temp.next
            temp.next = before #flips the arrow
            before = temp
            temp = after
        return before