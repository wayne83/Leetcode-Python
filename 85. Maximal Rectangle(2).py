class Solution(object):
    def maximalRectangle(self, matrix):
    	if len(matrix) > 0:
    		n = len(matrix)
    		m = len(matrix[0])
    		left = []
    		right = []
    		heights = []
    		maxs = 0
    		for i in range(n):
    			for j in range(m):
    				matrix[i][j] = int(matrix[i][j])
    		for i in range(0,m):
    			left.append(0)
    			right.append(m-1)
    			heights.append(0)
    		for i in range(0,n):
    			cur_left = 0;cur_right = m
    			for j in range(m):
    				if matrix[i][j] == 1 :
    					heights[j]+=1
    				else:
    					heights[j] = 0
    			for j in range(m):
    				if matrix[i][j] == 1:
    					left[j] = max(cur_left,left[j])
    				else:
    					left[j] = 0 ;cur_left = j + 1
    			for j in range(m)[::-1]:
    				if matrix[i][j] == 1:
    				 	right[j] = min(right[j],cur_right)
    				else:
    				 	right[j] = m;cur_right = j
    			for j in range(m):
    				maxs = max(maxs, (right[j]-left[j])*heights[j])
    		return maxs
    	else:
    		return 0	