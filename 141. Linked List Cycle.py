# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
        	return False
        p = head.next
        head.val = None
        while p!= None:
        	if p.val == None:
        		return True
        	else:
        		p.val = None
        		p = p.next
        return False

