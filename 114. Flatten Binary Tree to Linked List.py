# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global prev
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        global prev
        if root == None:
        	return 
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = prev
        root.left = None
        prev = root


