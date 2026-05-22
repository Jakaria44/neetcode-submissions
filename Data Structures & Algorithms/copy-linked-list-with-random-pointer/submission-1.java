/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node>nodeMap = new HashMap<>();
        Node curr = head;
        while(curr != null) {
            if(!nodeMap.containsKey(curr))
                nodeMap.put(curr, new Node(curr.val));
            curr = curr.next;
        }
        Node cp = nodeMap.get(head);
        curr = cp;
        while(head != null) {
            curr = nodeMap.get(head);
            curr.next = head.next == null? null :nodeMap.get(head.next);
            curr.random = head.random == null? null : nodeMap.get(head.random);

            head = head.next;
        }
        return cp;
    }
}
