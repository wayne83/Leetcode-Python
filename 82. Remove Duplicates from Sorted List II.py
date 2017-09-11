# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return None
        p = head
        ans = ListNode(0)
        ans.next = head
        pre = ans

        while p!=None：
        	while p.next!=None and p.next.val==p.val:
        		p = p.next
        	if pre.next == p:
        		pre = pre.next
        	else:
        		pre.next = p.next
        	p = p.next
        return ans