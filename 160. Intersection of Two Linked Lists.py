# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
        	return None
        p = headA
        nump = 1
        while p.next != None:
        	nump+=1
        	p = p.next
        q = headB
        numq = 1
        while q.next != None:
        	numq+=1
        	q = q.next
        p = headA
        q = headB
        if nump == numq:
        	return self.getNode(p,q)
        elif nump > numq:
        	for i in range(nump-numq):
        		p = p.next
        	return self.getNode(p,q)
        else:
        	for i in range(numq-nump):
        		q = q.next
        	return self.getNode(p,q)
    def getNode(self,headA,headB):
    	p = headA
    	q = headB
    	while q!=None and p!= None:
    		if q == p:
    			return p
    		q = q.next
    		p = p.next
    	return None