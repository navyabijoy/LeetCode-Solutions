# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        total = 0
        while temp:
            temp = temp.next
            total += 1
            
            

        if total < k:
            return head

        curr = head
        after = None
        before = None

        count = 0

        while curr is not None and count < k:
            after = curr.next 
            curr.next = before
            before = curr
            curr = after 
            count += 1
        
        if after is not None:
            head.next = self.reverseKGroup(after, k)
        
        return before
