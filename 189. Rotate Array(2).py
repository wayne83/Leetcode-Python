class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        step = n%k

        self.Reverse(nums,0,n-step)
        self.Reverse(nums,n-step,n)
        self.Reverse(nums,0,n)


    def Reverse(self,nums,start,end):
    	i = start
    	j = end-1
    	while i<j:
    		nums[i]^=nums[j]
    		nums[j]^=nums[i]
    		nums[i]^=nums[j]
    		i+=1
    		j-=1