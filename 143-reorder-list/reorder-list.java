/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    public void reorderList(ListNode head) {
        // steps to follow:
        // 1. find the middle node
        // 2. point the middle node next to none
        // 3. reverse the second half
        // 4. then place two pointers and merge
        if (head == null || head.next == null){
            return;
        }
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next!= null){
            slow = slow.next;
            fast = fast.next.next;
        }
        // now slow is the middle node
        ListNode second = slow.next;
        slow.next = null;
        
        second = reverse(second);

        ListNode p1 = head; // first half
        ListNode p2 = second; // second half
        while(p1 != null && p2 != null){
            ListNode temp1 = p1.next;
            ListNode temp2 = p2.next;
            p1.next = p2;
            p2.next = temp1;
            p1 = temp1;
            p2 = temp2;

        }
 
    }
    private ListNode reverse(ListNode node){
        ListNode curr = node;
        ListNode  before = null;
        while(curr!= null){
            ListNode after = curr.next;
            curr.next = before;
            before = curr;
            curr = after;
        }
        return before;
    }
}