# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        return self.isSameTree( root ,self.changeLeftAndRight( root ) )
    
    def changeLeftAndRight(self,root):
    	if root == None:
    		return root
        newroot = TreeNode(root.val)
        newroot.left = self.changeLeftAndRight(root.right)
        newroot.right = self.changeLeftAndRight(root.left)
    	return newroot 

    def isSameTree(self, p, q):
        if p == None or q == None:
        	if p == q:
        		return True
        	else:
        		return False
        if p.val == q.val:
        	return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
        	return False