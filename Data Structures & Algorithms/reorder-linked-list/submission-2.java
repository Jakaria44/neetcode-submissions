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
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return newHead;
    }
    public void reorderList(ListNode head) {
        // find mid point
        ListNode slow, fast;
        slow= fast = head;

        while(fast != null && fast.next != null ){
            slow = slow.next;
            fast = fast.next.next;
        }
        // slow is the last node of answer array

        ListNode reversed= reverseList(slow.next);
        slow.next = null;
        var curr = head;
        while(reversed!= null) { 
            // because 2nd half < 1st half
            var nextCurr = curr.next;
            var nextRev = reversed.next;

            curr.next = reversed;
            reversed.next = nextCurr;

            curr = nextCurr;
            reversed = nextRev;
        }

    }
}
