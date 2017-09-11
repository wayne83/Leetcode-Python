# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isValid(root,self.prev)
        
    def isValid(self,root,self.prev):
    	if root == None:
    		return True
    	if self.isValid(root.left,self.prev) == False:
    		return False
    	if self.prev != None and self.prev.val >= root.val:
    		return False
    	self.prev = root
    	return self.isValid(root.right,self.prev)