# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
    
        lheight = self.tree_height(root.left)
        rheight = self.tree_height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(lheight + rheight, max(ldiameter, rdiameter))
        

    def tree_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.tree_height(root.left), self.tree_height(root.right))