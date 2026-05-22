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
    public ListNode reverseList(ListNode head) {

        if(head == null || head.next == null) return head;


        ListNode current = head;
        ListNode prev = null;
        ListNode next = null;
        while(current != null) {

            // keep next node
            next = current.next;
            // reverse
            current.next = prev;

            // iterate
            //  current will be previous of next node
            prev = current;
            
            current = next;
        }

        return prev;
    }
}
