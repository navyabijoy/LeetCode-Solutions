# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
            
        if n == total:
            return head.next
        prev = head
        for _ in range(total - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head