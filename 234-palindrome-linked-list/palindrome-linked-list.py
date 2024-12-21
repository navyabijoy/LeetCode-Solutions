# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            before = None
            curr = head
            while curr:
                after = curr.next
                curr.next = before
                before = curr
                curr = after
            return before
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = reverse(slow) #slow was pointing at the middle node of the linked lsit
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev  = rev.next
        return True
    
        