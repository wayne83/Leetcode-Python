class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maps = {}
        while True:
        	ans = 0
        	while n != 0:
        		ans += (n%10)*(n%10)
        		n = n/10
        	if maps.has_key(ans):
        		return False
        	elif ans == 1:
        		return True
        	else:
        		maps[ans] = 1
        	n = ans