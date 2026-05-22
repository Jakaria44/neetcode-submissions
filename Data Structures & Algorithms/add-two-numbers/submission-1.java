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

    ListNode reverse(ListNode head){
        if (head == null || head.next == null) return head;

        var newHead = reverse(head.next);

        head.next.next = head;
        head.next = null;

        return newHead;
    }


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         
        ListNode ans = new ListNode();
        ListNode curr = ans;

        int rm = 0;
        while(l1 != null || l2 != null || rm != 0) {
            int sum =(l1 == null ? 0: l1.val )+ (l2 == null? 0 : l2.val) + rm;
            
            curr.next = new ListNode( sum%10 );

            curr = curr.next;
            if(l1 != null) l1 = l1.next;
            if(l2  != null) l2 = l2.next;
            rm = sum / 10;
        }
        

        return  ans.next;

    }
}
