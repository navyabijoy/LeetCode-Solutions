# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwo(self, head1, head2):
        t1 = head1
        t2 = head2
        dummy = ListNode(-1)
        curr = dummy
        while t1 and t2:
            if t1.val < t2.val:
                curr.next = t1
                t1 = t1.next
            else:
                curr.next = t2
                t2 = t2.next
            curr = curr.next
        if t1:
            curr.next = t1
        if t2:
            curr.next = t2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merge = []
            for i in range(0, len(lists), 2): # merging 2 and 2 then combining
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merge.append(self.mergeTwo(l1,l2))
            lists = merge
        return lists[0]