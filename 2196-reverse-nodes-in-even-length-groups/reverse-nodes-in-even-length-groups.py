# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        group_len = 2
        while prev.next:
            node = prev 
            num_nodes = 0
            for i in range(group_len):
                if not node.next:
                    break
                num_nodes += 1
                node = node.next
            if num_nodes % 2:
                prev = node
            else:
                reverse = node.next
                curr = prev.next
                for j in range(num_nodes):
                    curr_next = curr.next
                    curr.next = reverse
                    reverse = curr
                    curr = curr_next
                prev_next = prev.next
                prev.next = node
                prev = prev_next
            group_len += 1
        return head