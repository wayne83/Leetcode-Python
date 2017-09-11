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
        p = head
        pre = head
        while p!=None and p.next!=None:
        	if p.next == p:
        		return True
        	p = p.next
        	pre.next = pre
        	pre = p
        return False