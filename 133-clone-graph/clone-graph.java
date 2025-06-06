/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null){
            return null;
        }
        Map<Node, Node> nodesCompleted = new HashMap<>();
        return helper(node, nodesCompleted);
    }
    private Node helper(Node root, Map<Node, Node>nodesCompleted){
        if(root == null){
            return null;
        }
        // if node is already cloned
        if(nodesCompleted.containsKey(root)){
            return nodesCompleted.get(root);
        }

        Node copy = new Node(root.val);
        nodesCompleted.put(root,copy);

        for(Node neighbor : root.neighbors){
            copy.neighbors.add(helper(neighbor, nodesCompleted));
        }
        return copy;
    }
}