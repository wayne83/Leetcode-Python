class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = 0 
        for i in range(len(nums))
        	temp = now
        	now = max(last+nums[i],now)
        	last = temp
        return now