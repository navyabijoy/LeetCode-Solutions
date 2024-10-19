# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse 'k' nodes starting from `head`
        def reverse_k_nodes(head, k):
            prev = None
            curr = head
            for _ in range(k):
                if not curr:
                    return None, head  # If fewer than `k` nodes, return the original head
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, curr  # Return the new head of the reversed list, and the next node after k nodes

        # Check if there are at least `k` nodes to reverse
        temp = head
        for i in range(k):
            if not temp:
                return head  # If fewer than `k` nodes, return the head as is
            temp = temp.next

        # Reverse the first `k` nodes
        new_head, next_group_head = reverse_k_nodes(head, k)

        # Recursively reverse the remaining list and connect
        if next_group_head:
            head.next = self.reverseKGroup(next_group_head, k)

        return new_head