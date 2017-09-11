class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
        	temp = []
        	for j in range(i+1):
        		if j == 0 or j == i:
        			temp.append(1)
        		else:
        			temp.append(ans[i-1][j]+ans[i-1][j-1])
        	ans.append(temp)
        return ans