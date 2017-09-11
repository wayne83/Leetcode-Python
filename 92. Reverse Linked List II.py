# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        if head == None:
        	return head
        ans = ListNode(0)
        ans.next = head
        p = ans
        for i in range(m-1):
        	p = p.next
        cur = p.next
        for i in range(m-n):
        	move = cur.next
        	cur.next = move.next
        	move.next = p.next 
        	p.next = move
        return ans.next
        		

