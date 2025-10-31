# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # find middle of LL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is in the center
        second_half = self.reverseLL(slow)
        
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True