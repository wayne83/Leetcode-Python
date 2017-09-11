# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
        	return None
        treearr = []
        p = head
        while p!=None:
        	treearr.append(p.val)
        	p = p.next
        return self.toTree(treearr)

    def toTree(self,treearr):
    	if len(treearr) == 0 :
    		return None
    	mid = len(treearr)/2
    	head = TreeNode(treearr[mid])
    	head.left = self.toTree(treearr[:mid])
    	head.right = self.toTree(treearr[mid+1:])
    	return head