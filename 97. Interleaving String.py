class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        table = [ [False]*(len(s1)+1) ] * (len(s2)+1)

        if len(s1)+len(s2) != len(s3):
        	return False
        for i in range( len(s1)+1 ):
        	for j in range( len(s2) + 1):
        		if i==0 and j == 0:
        			table[i][j] =  True
        		elif i == 0:
        			table[i][j] =  table[i][j-1] and s2[j-1] == s3[i+j-1]
        		elif j == 0:
        			table[i][j] =  table[i-1][j] and s1[i-1] == s3[i+j-1]
        		else:
        			table[i][j] =  (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
        return table[len(s1)][len(s2)]