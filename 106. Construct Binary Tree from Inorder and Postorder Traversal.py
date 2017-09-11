# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder :
        	mid = inorder.index(postorder.pop())
        	root = TreeNode(inorder[mid])
        	root.right = self.buildTree(inorder[mid+1:],postorder)
        	root.left = self.buildTree(inorder[0:mid],postorder)
        	return root