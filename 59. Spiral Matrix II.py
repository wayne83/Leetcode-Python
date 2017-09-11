class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [ ([1]*n) for i in range(n) ]
        i = 0
        nums = 1
        while n>=0:
        	for j in range(n):
        		ans[i][j+i] = nums
        		nums+=1
        	for j in range(n-1):
        		ans[j+i+1][i+n-1] = nums
        		nums+=1
        	for j in range(n-1):
        		ans[i+n-1][ i+n-2-j] = nums
        		nums+=1
        	for j in range(n-2):
        		ans[i+n-2-j][i] = nums
        		nums+=1 
        	n=n-2
        	i+=1
        return ans

