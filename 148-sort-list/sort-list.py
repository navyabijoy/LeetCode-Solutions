# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. find the middle
    2. seperate the middle (left linked list) and middle.next(right LL)
    3. merge sort both the lists
    4. combine the two lists
    '''
    

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findMiddle(head):
            if head is None or head.next is None:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def mergeTwoSortedLinkedLists(head1, head2):
            dummy = ListNode()
            curr = dummy

            p1 = head1
            p2 = head2

            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            if p1 is None:
                curr.next = p2
            if p2 is None:
                curr.next = p1
            
            return dummy.next

        if not head or not head.next:
            return head

        mid = findMiddle(head)
        
        temp2 = mid.next
        mid.next = None
        temp1 = head

        temp1 = self.sortList(temp1)
        temp2 = self.sortList(temp2)

        return mergeTwoSortedLinkedLists(temp1, temp2)

