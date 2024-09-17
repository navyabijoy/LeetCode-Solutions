# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy
        
        # Pointers for traversing the lists
        p1 = list1
        p2 = list2
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # If there are remaining nodes in list1
        if p1 is not None:
            current.next = p1
        
        # If there are remaining nodes in list2
        if p2 is not None:
            current.next = p2
        
        # The head of the merged list is next to the dummy node
        return dummy.next
