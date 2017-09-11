class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = 0 if len(matrix) == 0 else len(matrix[0])

        start = m-1
        for i in range(m-1):
        	if matrix[i][0] <= target and matrix[i+1][0] > target:
        		start = i
        
        
        for i in range(n):
        	if matrix[start][i] == target:
        		return True
        return False