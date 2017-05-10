class Solution(object):
    def isScramble(self, s1, s2,memo={}):
        if len(s1) != len(s2):
        	return False
        if len(s1) == 1:
        	return s1 == s2
        if (s1,s2) in memo:
        	return memo[s1,s2]
        for i in range(1,len(s1)):
        	if( (self.isScramble(s1[:i],s2[-i:],memo) and self.isScramble( s1[i:],s2[:-i],memo )) or
        		(self.isScramble(s1[:i],s2[:i],memo) and self.isScramble( s1[i:],s2[:-i],memo )) ):
        		memo[s1,s2] = True
        		return True
        memo[s1,s2] = False
        return False

        