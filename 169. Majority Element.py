class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
        	dic[i] = dic.get(i,0) + 1
        size = len(nums)
        for k,v in dic.items():
        	if v>(size//2):
        		return k