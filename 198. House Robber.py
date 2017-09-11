class Solution(object):

	
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        ans = [0]* (len(nums)+1)
        if len(nums) <= 2:
        	return nums[0] if len(nums) == 1 else max(nums[0],nums[1])
        else:
        	ans[1] = nums[0]
        	for i in range(2,len(nums)+1):
        		ans[i] = max( nums[i-1] + ans[i-2],ans[i-1])
        	return ans[len(nums)]

