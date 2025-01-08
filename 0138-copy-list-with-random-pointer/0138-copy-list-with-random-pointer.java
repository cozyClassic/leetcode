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
        if (Objects.isNull(head)) return null;
        Node oldCurr = head;
        Node newCurr = new Node(oldCurr.val);
        Node newHead = newCurr;
        HashMap<Node,Node> map = new HashMap<>();

        while (!Objects.isNull(oldCurr.next)) {
            map.put(oldCurr, newCurr);
            newCurr.random = oldCurr;
            newCurr.next = new Node(oldCurr.next.val);
            newCurr = newCurr.next;
            oldCurr = oldCurr.next;
        }
        map.put(oldCurr, newCurr);
        newCurr.random = oldCurr;

        newCurr = newHead;

        while (!Objects.isNull(newCurr.next)) {
            newCurr.random = map.get(newCurr.random.random);
            newCurr = newCurr.next;
        }
        newCurr.random = map.get(newCurr.random.random);

        return newHead;
    }
}