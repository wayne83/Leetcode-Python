class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        m = len(num1)
        n = len(num2)

        pos = [0] * (m+n)
        for i in range(m)[::-1]:
        	for j in range(n)[::-1]:
        		p1 = i+j
        		p2 = i+j+1
        		sum = int(num1[i]) * int(num2[j]) + pos[p2]
        		pos[p2] = sum%10 
        		pos[p1] += sum/10

        ans = ""
        for i in range(len(pos)):
        	if (len(ans)==0 and pos[i] == 0) == False:
        		ans+=str(pos[i])
        return "0" if len(ans)==0 else ans