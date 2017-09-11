class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       	if len(prices) == 0:
       		return 0
       	min = prices[0]
       	ans = 0
       	for i in range(len(prices)):
       		if prices[i] < min:
       			min = prices[i]
       		else:
       			ans += prices[i] - min
       			min = prices[i]
       	return ans