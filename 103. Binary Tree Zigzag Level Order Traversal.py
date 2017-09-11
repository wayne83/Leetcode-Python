# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.zigzagL(root,1,ans)
        return ans
        
        
    def zigzagL(self,root,level,ans):
    	if root == None:
    		return 
    	if level > len(ans):
    		temp = [root.val]
    		ans.append(temp)
    	else:
    		if level%2 == 0:
    			ans[level-1].insert(0,root.val)
    		else:
				ans[level-1].append(root.val)
    	self.zigzagL(root.left,level+1,ans)
    	self.zigzagL(root.right,level+1,ans)
    	return ans