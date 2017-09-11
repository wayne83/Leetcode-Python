class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        zero_i = []
        zero_j = []
        m = len(matrix)
        n = 0 if m==0 else len(matrix[0])
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			zero_i.append(i)
        			zero_j.append(j)
        for i in range(len(zero_i)):
        	for j in range(n):
        		matrix[zero_i[i]][j] = 0
        for i in range(len(zero_j)):
        	for j in range(m):
        		matrix[j][zero_j[i]] = 0