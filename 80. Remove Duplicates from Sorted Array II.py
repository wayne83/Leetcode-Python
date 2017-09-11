class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        ans = 0
        if len(nums) == 0 :
        	return ans
        old = nums[0]
        size = len(nums)
        j=0
        for i in range(size):
        	if nums[i] == old:
        		count+=1
        	else:
        		count = 1
        	if count <= 2:
        		ans+=1
        		nums[j] = nums[i]
        		j+=1
        	old = nums[i]
        return ans