# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self,head):
        prev, curr = None, head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse_linked_list(slow)
        first_half = head
        max_sum = float('-inf')
        while second_half:
            curr_sum = first_half.val + second_half.val
            max_sum = max(max_sum, curr_sum)
            first_half = first_half.next
            second_half = second_half.next
        return max_sum