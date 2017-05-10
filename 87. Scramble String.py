class Solution(object):
    def isScramble(self, s1, s2,memo={}):
    	count = [0]*26
        if len(s1) != len(s2):
        	return False
        if len(s1) <= 1:
        	return s1 == s2
        for i in range(len(s1)):
        	count[ ord(s1[i])- ord('a') ]+=1
        	count[ ord(s2[i])- ord('a') ]-=1
        for i in range(26):
        	if count[i] != 0 :
        		return False
        for i in range(1,len(s1)):
        	if( (self.isScramble(s1[:i],s2[-i:]) and self.isScramble( s1[i:],s2[:-i])) or
        		(self.isScramble(s1[:i],s2[:i]) and self.isScramble( s1[i:],s2[i:])) ):
        		return True
        return False

        