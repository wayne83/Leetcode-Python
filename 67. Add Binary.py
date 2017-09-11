class Solution(object):
	def addBinary(self, a, b):
		la = len(a);lb = len(b)
		yu = 0
		ans = ""
		i = 0
		while i <= la-1 or i <= lb-1:
			if (la-i-1) >= 0 and (lb-i-1)>= 0:
				he = int(a[la-i-1]) + int(b[lb-i-1]) + yu 
				print he
			elif (la-i-1) >= 0:
				he = int(a[la-i-1]) + yu 
			else:
				he = int(b[lb-i-1]) + yu
			yu =  he / 2
			he =  he % 2 
			ans = str(he) + ans
			i+=1
		if yu != 0 :
			ans = str(1) + ans
		return ans