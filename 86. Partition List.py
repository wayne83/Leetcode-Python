# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        if head == None:
        	return None
        minnode = ListNode(0)
        maxnode = ListNode(0)
        temp_min = minnode
        temp_max = maxnode
        p = head

        while p!=None:
        	if p.val < 3:
        		temp_min.next = p
        		temp_min = p
        		p = p.next
        		temp_min.next = None
        	else:
        		temp_max.next = p
        		temp_max = p
        		p = p.next
        		temp_max.next = None
        temp_min.next = maxnode.next
        return minnode.next