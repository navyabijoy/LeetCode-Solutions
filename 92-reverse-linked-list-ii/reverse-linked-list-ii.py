# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == 0:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range (left-1):
            prev = prev.next

        current = prev.next

        for i in range(right-left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        head = dummy.next
        return dummy.next

