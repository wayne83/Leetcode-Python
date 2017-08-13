# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        list = []
        for i in range(n):
            list.append(i+1)
        return self.newTrees(n,list)
    

    def newTrees(self,n,list):
        listtn = []
        if n == 0:
            return listtn
        elif n == 1:
            tn = TreeNode(list[0])
            listtn.append(tn)
            return listtn
        else:
            
            print ("n",n)
            for i in range(n):
                leftlist = self.newTrees(i,list[:i])
                
                #if (n-i-1)!=len(list[i+1:]):
                print ("ern:",n," i:",i)
                rightlist = self.newTrees(n-i-1,list[i+1:])

                if len(leftlist) == 0:
                    for j in range(len(rightlist)):
                        tn = TreeNode(list[i])
                        tn.left = None
                        tn.right = rightlist[j]
                        listtn.append(tn)

                if len(rightlist) == 0:
                    for j in range(len(leftlist)):
                        tn = TreeNode(list[i])
                        tn.left = leftlist[j]
                        tn.right = None
                        listtn.append(tn)

                for m in range(len(leftlist)):
                    for j in range(len(rightlist)):
                        tn = TreeNode(list[i])
                        tn.left = leftlist[m]
                        tn.right = rightlist[j]
                        listtn.append(tn)
            return listtn

test = Solution()
print( test.generateTrees(5) )