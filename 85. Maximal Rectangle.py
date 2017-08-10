class Solution(object):
    def maximalRectangle(self, matrix):
    	if len(matrix) > 0:
    		ans = self.largestRectangleArea(matrix[0])
    		print(ans)
    		for i in range(1,len(matrix)):
    			for j in range(len(matrix[i])):
    				if int(matrix[i][j]) != 0 :
    					matrix[i][j] = int(matrix[i-1][j]) + 1
    				else:
    					matrix[i][j] = 0
    				print matrix[i][j],	
    			temp = self.largestRectangleArea(matrix[i])	
    			print("temp:" + temp)
    			ans = max(ans,self.largestRectangleArea(matrix[i]))
    			print("nextans:" + ans)
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

