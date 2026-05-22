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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        

        // always include this for the case when 
        // head is removed;
        ListNode answer = new ListNode();

        answer.next = head;
        ListNode lag, lead;
        lead = lag = answer;
        

        for(int i = 0; i< n; i++) {
            lead = lead.next;
            if(lead == null) return head;
        }

        while(lead.next != null) {
            lead = lead.next; 
            lag = lag.next;
        }
        // now lag points to the previous of 'to be removed' node
        
        lag.next = lag.next.next;

        return answer.next;
    }
}
