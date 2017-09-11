# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
        	return head
        p = head 
        len = 1
        while p.next!=None:
        	len+=1
        	p = p.next
        step = 0 if len == 0 else k%len

        if step == 0:
        	return head
        p.next = head
        p = head
        start = head
        for i in range(len-step-1):
        	p = p.next 
        head = p.next
        p.next = None
        return head
