# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        store = set()
        # storing the node itself, by iterating one of the lists entirely
        while headA:
            store.add(headA)
            headA = headA.next

        # iterating through the other list, if that node is present then it returns that node
        while headB:
            if headB in store:
                return headB
            headB = headB.next
        return None
