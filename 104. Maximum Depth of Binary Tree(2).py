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
        if root == None:
        	return 0
        maxans = 0
        value = []
        treeStack = []
        treeStack.append(root)
        value.append(1)
        while len(treeStack) != 0:
        	temp = value.pop()
        	maxans = max(maxans,temp)
        	temp_tree = treeStack.pop()
        	if temp_tree.left != None:
        		treeStack.append(temp_tree.left)
        		value.append(temp+1)
        	if temp_tree.right != None:
        		treeStack.append(temp_tree.right)
        		value.append(temp+1)
        return maxans