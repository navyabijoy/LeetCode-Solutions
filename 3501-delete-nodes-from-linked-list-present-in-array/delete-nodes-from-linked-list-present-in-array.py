# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num = set(nums)

        while head and head.val in num:
            head = head.next
        
        if not head:
            return None

        curr = head

        while curr and curr.next:
            if curr.next.val in num:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head