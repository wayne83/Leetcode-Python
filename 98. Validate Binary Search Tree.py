# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root,-100000,sys.maxint)

    def isValid(self,root,minval,maxval):
    	if root == None:
    		return True
    	if root.val <= minval or root.val >= maxval:
    		return False
    	return self.isValid(root.left,minval,root.val) and self.isValid(root.right,root.val,maxval)
    	

