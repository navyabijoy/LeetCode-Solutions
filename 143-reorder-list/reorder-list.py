# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # second half of the node
        slow.next = None #middle node will become the last node after merging
        prev = None
        #reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merging the lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next= second
            second.next = temp1
            first, second = temp1, temp2
        return head
