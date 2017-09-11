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
        queue = [root]
        ans = 0
        while len(queue) != 0:
        	size = len(queue)
        	for i in range( size ):
        		temp_tree = queue[0]
        		del queue[0]
        		if temp_tree.left != None:
        			queue.append(temp_tree.left)
        		if temp_tree.right != None:
        			queue.append(temp_tree.right)
        	ans+=1
        return ans