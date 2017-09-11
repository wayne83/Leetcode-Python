class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        if len(nums) == 0 :
        	return False
        
        left = 0 
        right = len(nums)-1
        while left != right:
        	mid = (left+right)//2
        	if nums[mid] > nums[left]:
        		if target >= nums[left] and target <= nums[mid]:
        			right = mid
        		else:
        			left = mid + 1
        	elif nums[mid] < nums[left]:
        		if target>nums[mid] and target<=nums[right]:
        			left = mid+1
        		else:
        			right = mid
        	else:
        		if target == nums[mid]:
        			return True
        		else:
        			mid = left + 1
        return nums[right] == target



