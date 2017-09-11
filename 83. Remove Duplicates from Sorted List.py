# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if head == None:
			return None
		pre = head
		cur = head.next
		while cur != None:
			if pre.val == cur.val:
				pre.next = cur.next
				cur = cur.next
			else:
				pre = cur
				cur = cur.next
		return head