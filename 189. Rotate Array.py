class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        step = k % len(nums)
        count = 0 
        start = 0
        while count!=len(nums):
        	cur = start
        	prev = nums[start]
        	while True: 
        		next = (i+step)%len(nums)
        		nums[next] = prev^nums[next]
        		prev = nums[next] ^ prev
        		nums[next] = nums[next] ^ prev
        		count++
        		cur = next
        		if start == cur:
        			break
        	start++
        return nums