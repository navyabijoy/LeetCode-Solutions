# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        total = 1
        tail = head
        while tail.next:
            total += 1
            tail = tail.next

        k = k % total

        if k == 0:
            return head

        tail.next = head # make it circular
        step_to_new_head = total - k - 1
        new_tail = head
        for _ in range(step_to_new_head):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        