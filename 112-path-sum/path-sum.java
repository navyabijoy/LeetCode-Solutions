/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean helper(TreeNode current, int targetSum, int total){
        if(current == null){
            return false;
        }
        total = total + current.val;
        if(current.left == null && current.right == null){
            return (total == targetSum);
        }
        return helper(current.left, targetSum, total) || helper(current.right, targetSum, total);

    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return helper(root, targetSum, 0);
    }
}