class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        liststr = []
        s = s.lower()
        for i in range(len(s)):
        	n = ord(s[i])-ord("a")
        	z = ord(s[i])-ord("0")
        	if (n>=0 and n<26) or (z>=0 and z<=9):
        		liststr.append(s[i])

        size = len(liststr)
       	for i in range( size//2 ):
       		if liststr[i] != liststr[size-1-i]:
       			return False
       	return True