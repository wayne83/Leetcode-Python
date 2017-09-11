class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        step = k%n
        nums1 = nums[n-step:]
        for i in range(n-step):
        	nums1.append(nums[i])
        for i in range(n):
            nums[i] = nums1[i]