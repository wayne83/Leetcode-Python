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
        value = [sum]
        stack = [root]
        while len(stack) != 0:
        	temp_tree = stack.pop()
        	temp = value.pop()
        	if temp_tree.left == None and temp_tree.right == None:
        		if temp == temp_tree.val:
        			return True
        	if temp_tree.left!=None:
        		stack.append(temp_tree.left)
        		value.append(temp - temp_tree.val)
        	if temp_tree.right!=None:
        		stack.append(temp_tree.right)
        		value.append(temp-temp_tree.val)
       	return False