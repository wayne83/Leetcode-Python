class Solution(object):
    def maximalRectangle(self, matrix):
    	if len(matrix) > 0:
    		ans = 0
    		print(ans)
    		for i in range(0,len(matrix)):
    			for j in range(len(matrix[i])):
    				matrix[i][j] = int(matrix[i][j])
    				if i != 0 and int(matrix[i][j]) != 0 :
    					matrix[i][j] = int(matrix[i-1][j]) + 1
    				print matrix[i][j],	
    			temp = self.largestRectangleArea(matrix[i])	
    			ans = max(ans,self.largestRectangleArea(matrix[i]))
    		return ans		
    	else:
    		return 0 


    def largestRectangleArea(self,heights):
     	heights.append(0)
     	stack = [-1]
     	ans = 0
     	for i in range(len(heights)):
     		print heights[i],
     		while heights[i] < heights[ stack[-1] ]:
     			h = heights[ stack.pop() ]
     			w = i-1-stack[-1]
     			ans = max(ans,h*w)
     		stack.append(i)	
     	return ans

