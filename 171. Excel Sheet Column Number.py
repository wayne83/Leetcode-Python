class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0
        mi = 1 
        for i in range( len(s) ):
        	ans = mi*ans + ( ord(s[i])-ord("A") + 1 )
        	print ans
        	mi = mi*26
        return ans