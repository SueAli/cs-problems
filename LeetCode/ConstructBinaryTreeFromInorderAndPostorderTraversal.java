/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructBinaryTreeFromInorderAndPostorderTraversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        
        Map<Integer, Integer> inOrderIdx = new HashMap<Integer, Integer>();
        
        for(int i =0; i < inorder.length; i++) {
            inOrderIdx.put(inorder[i], i);
        }
        
        return buildTreeRec(inorder, postorder,
                            0, inorder.length - 1,
                            0, postorder.length - 1,
                            inOrderIdx);
    }
    
    private TreeNode buildTreeRec(int[] inorder, int[] postorder,
                                 int inStart, int inEnd,
                                 int postStart, int postEnd,
                                 Map<Integer, Integer> inOrderIdx) {
     
        if (inEnd < inStart || postEnd < postStart) {
            return null;
        }
        
        // Find the root from the postOrder tree. It should be the last element in the array
        int rootVal = postorder[postEnd];
        int rootIdxInorder = inOrderIdx.get(rootVal);
        
        // Find the right and left subtree boundaries
        //  Find the left subtree length from the inorder tree
        int leftLen = rootIdxInorder - inStart;
        //  Find the right subtree length from the inorder tree
        int rightLen = inEnd - rootIdxInorder;
        
        TreeNode root = new TreeNode(rootVal);
        
        // Use these lengths to get the postTree boundries
        root.left = buildTreeRec(inorder, postorder, inStart, rootIdxInorder -1,
                                postEnd - rightLen - leftLen, postEnd - rightLen -1, inOrderIdx);
        root.right = buildTreeRec(inorder, postorder, rootIdxInorder + 1, inEnd,
                                 postEnd - rightLen, postEnd - 1, inOrderIdx);
        return root;
        
    }
}
