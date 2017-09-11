# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        self.pathSumAns(root,sum,ans,temp)
        return ans

    def pathSumAns(self,root,sum,ans,temp):
   		if root == None:
   			return
   		temp.append(root.val)
   		if root.left == None and root.right == None and root.val == sum:
   			temp_arr = temp[:]
   			ans.append(temp_arr)
   			temp.pop()
   			return
   		else:
   			self.pathSumAns(root.left,sum-root.val,ans,temp)
   			self.pathSumAns(root.right,sum-root.val,ans,temp)
   		temp.pop()
