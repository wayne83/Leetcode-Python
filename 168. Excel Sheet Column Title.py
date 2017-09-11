class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = []
        for i in range(26):
        	str.append( chr(ord("A")+i) )

        while n!=0:
        	ans = str[(n-1)%26] + ans
        	n = (n-1)//26

        return ans