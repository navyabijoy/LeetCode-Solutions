# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
        
        if total < k:
            return head
        prev = None
        curr = head
        count = 0
        while curr and count != k:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
            count += 1
        
        
        if after is not None:
            head.next = self.reverseKGroup(after, k)
        
        return prev # its now the head
        
