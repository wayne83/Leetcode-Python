class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums0 = 0
        nums1 = 0
        for i in range(len(nums)):
        	if nums[i] == 0:
        		del nums[i]
        		nums0+=1
        		nums.insert(0,0)
        	elif nums[i] == 1:
        		del nums[i]
        		nums.insert(nums0,1)
        		nums1+=1
        	else:
        		del nums[i]
        		nums.insert(nums0+nums1,2)
		return nums