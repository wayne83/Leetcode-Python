class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        strlist = path.split("/")
        stack = []
        for i in range(len(strlist)):
        	print(strlist[i])
        	if strlist[i] == "..":
        		if len(stack) != 0:
        			stack.pop()
        	elif strlist[i] != "." and strlist[i] != "":
        		stack.append(strlist[i])
        if len(stack)==0:
        	return "/"
       	ans=""
       	for i in range(len(stack))
			ans = ans +  "/"  + stack[i]	
        return ans