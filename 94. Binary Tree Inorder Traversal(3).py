# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        list_tree = []

        cur = root
        while cur!=None or len(list_tree)!=0:
        	while(cur != None):
        		list_tree.append(cur)
        		cur = cur.left
        	temp = list_tree.pop()
        	ans.append(temp.val)
        	cur = temp.right
        return ans