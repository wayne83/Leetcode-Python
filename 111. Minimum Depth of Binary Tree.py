# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0

        if root.left!=None and root.right!=None:
        	return min(1+self.minDepth(root.left),1+self.minDepth(root.right))
        else:
        	return self.minDepth(root.left)+self.minDepth(root.right)+1