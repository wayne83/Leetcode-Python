class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = 0 if m==0 else len(matrix[0])

        l = 0 
        r = m*n-1
        while(l!=r)
        	mid = (l+r)//2
        	if matrix[mid//n][mid%n] < target:
        		l = mid + 1
        	else:
        		r = mid
        return matrix[mid//n][mid%n] == target