class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        ans = 0
        min = sys.maxint
        for i in range(n):
        	if prices[i] < min:
        		min = prices[i]
        	else:
        		temp = prices[i] - min
        		ans =  temp if temp>ans else ans
        return ans
