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
    Map<Node, Node>nodeMap ;
    public Node copyRandomList(Node head) {
        if(head == null) return null;
        nodeMap = new HashMap<>();
        nodeMap.put(head, new Node(head.val));

        Node curr = head;
        while(curr != null) {
            Node copy = nodeMap.get(curr);
            copy.next = processNode(curr.next);
            copy.random = processNode(curr.random);

            curr = curr.next;
        }
        return nodeMap.get(head);
    }

    public Node processNode(Node node){
        if(node == null) return null;

        if(!nodeMap.containsKey(node)) {
            Node newNode = new Node(node.val);
            nodeMap.put(node, newNode);
        }
        return nodeMap.get(node);
    }
}

