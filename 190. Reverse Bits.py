class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        lists = bin(n).replace("0b","")
        return int(lists.zfill(32)[::-1],base=2)