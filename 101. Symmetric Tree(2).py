# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.LeftAndRight(root.left,root.right)

    def LeftAndRight(self,left,right):
    	if left==None or right == None:
    		return left==right
    	else:
    		if left.val == right.val:
    			return self.LeftAndRight(left.left,right.right) and self.LeftAndRight(left.right,right.left)
    		else:
    			return False