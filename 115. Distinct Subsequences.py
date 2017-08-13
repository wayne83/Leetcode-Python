class Solution(object):
	def numDistinct(self, s, t):
		table = [ ([0] * (len(t)+1) ) for i in  range(len(s)+1)]
		for i in range( len(s)+1 ):
			table[i][0] = 1
		for i in range(1,len(s)+1 ):
			for j in range(1,len(t)+1 ):
				if s[i-1] == t[j-1]:
					table[i][j] = table[i-1][j-1] + table[i-1][j]
				else:
					table[i][j] = table[i-1][j]
		return table[len(s)][len(t)]