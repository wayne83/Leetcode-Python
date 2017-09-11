# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.levelO(root,1,ans)
        return ans

    def levelO(self,root,level,ans):
    	if root == None:
    		return 
    	if level > len(ans):
    		temp = [root.val]
    		ans.append(temp)
    	else:
    		ans[level-1].append(root.val)
    	self.levelO(root.left,level+1,ans)
    	self.levelO(root.right,level+1,ans)
    	
    	return ans