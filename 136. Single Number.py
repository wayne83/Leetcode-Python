class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        for i in range(len(nums)-1):
        	ans = ans ^ nums[i+1]
        if (n-1)%2 != 0:
        	ans=ans^0
        return ans
