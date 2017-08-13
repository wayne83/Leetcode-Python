class Solution(object):
	def numTrees(self, n):
		if n == 0 :
			return 0
		ans = [0]*(n+1)
		ans[1] = 1
		ans[0] = 1
		for i in range(2,n+1):
			print(i)
			for j in range(1,i+1):
				ans[i] = ans[i] + ans[i-j]*ans[j-1]
		return ans[n]


test = Solution()
print(test.numTrees(4))