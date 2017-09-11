# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead
        p = newhead.next
        while p!=None:
        	if p.val == val:
        		pre.next = p.next
        	else:
        		pre = p
        	p = p.next
        return newhead.next

