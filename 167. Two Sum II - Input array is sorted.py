class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(numbers)):
        	if target-numbers[i] in map:
        		return [map[target-numbers[i]],i+1]
        	else:
        		map[numbers[i]] = i+1