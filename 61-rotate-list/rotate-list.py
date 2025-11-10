# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or not head.next:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        
        tail.next = head
        steps = length - k
        newTail = head
        for _ in range(steps-1):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead
        

