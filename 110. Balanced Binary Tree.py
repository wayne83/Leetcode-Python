# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def  isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    	if root == None:
    		return True
    	if abs(self.getDepth(root.left) - self.getDepth(root.right) )<= 1:
    		return self.isBalanced(root.left) and self.isBalanced(root.right)
    	else:
    		return False

    def getDepth(self,root):
    	if root == None:
    		return 0
    	ans = 0
    	if root.left!=None or root.right!=None:
    		ans = 1 + max(self.getDepth(root.left),self.getDepth(root.right))
    		return ans
    	else:
    		return 1