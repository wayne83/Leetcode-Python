class Solution(object):
	def numDistinct(self, s, t):

		dp = ( [1]*(len(s)+1) )

		for i in range(1,len(t)+1):
			new_dp = ( [0]*(len(s)+1) )
			for j in range(1,len(s)+1):
				if s[j-1] == t[i-1]:
					new_dp[j] = new_dp[j-1] + dp[j-1]
				else:
					new_dp[j] = new_dp[j-1]
			dp = new_dp
		return dp[len(s)] 				
