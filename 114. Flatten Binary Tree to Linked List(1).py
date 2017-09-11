# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root != None:
            if root.left and root.right:
                temp = root.left
                while temp.right != None:
                    temp = temp.right
                temp.right = root.right

            if root.left:
                root.right = root.left
            root.left = None
            root = root.right



