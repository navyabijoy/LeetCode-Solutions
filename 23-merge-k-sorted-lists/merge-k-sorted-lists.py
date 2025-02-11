# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        min_heap = []
        for lst in lists:

            while lst is not None:
                min_heap.append(lst.val)
                lst = lst.next

        heapq.heapify(min_heap)
        merge = []
        for i in range(len(min_heap)):
            merge.append(heapq.heappop(min_heap))
        # creating a list?
        dummy = ListNode(-1)
        curr = dummy
        for i in range(len(merge)):
            new_node = ListNode(merge[i])
            temp = new_node
            curr.next = temp
            curr = temp
            temp = temp.next
        return dummy.next
