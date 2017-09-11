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
        if root==None:
        	return list_tree
        list_tree.append(root)
        while len(list_tree)!=0:
            temp = list_tree[len(list_tree)-1]
            if temp.left == None:
                list_tree.pop()
                ans.append(temp.val)
                while len(list_tree)!=0 and temp.right==None:
                    temp = list_tree.pop()
                    ans.append(temp.val)
                if temp.right != None:
                    list_tree.append(temp.right)
            else:
                list_tree.append(temp.left)
        return ans




