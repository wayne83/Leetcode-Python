# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root == None:
        	return False
        if root.Left == None and root.right==None and sum == root.val:
        	return True

        return hasPathSum(root.right,sum-root.val) or hasPathSum(root.left,sum-root.val)
