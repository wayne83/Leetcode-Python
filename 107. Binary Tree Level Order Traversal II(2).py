# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = []
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.DFS(root,0)
        return self.ans
        
    def DFS(self,root,level):
    	if root == None:
    		return 
    	if len(self.ans) == level:
    		print "123"
    		self.ans.append([])
    	ans[level].append(root.val)
    	self.DFS(root.left,level+1)
    	self.DFS(root.right,level+1)
