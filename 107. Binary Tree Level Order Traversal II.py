# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
        	return None
        queue = [root]
        ans = [[]]

        while len(queue) != 0:
        	count = []
        	size = len(queue)
        	for i in range(size):
        		temp_tree = queue[0]
        		del queue[0]
        		if temp_tree.left != None:
        			queue.append(temp_tree.left)
        		if temp_tree.right != None:
        			queue.append(temp_tree.right)
        		count.append(temp_tree.val)
        	ans.append(count)
        return ans[::-1][:-1]