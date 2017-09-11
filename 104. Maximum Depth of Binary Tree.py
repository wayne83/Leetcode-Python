# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root == None:
        	return ans
        else:
        	ans = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right) )
        	return ans