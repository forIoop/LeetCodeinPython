class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            #Adds a '1' if there are 2 1's stacked on each other, else shifts n right one space
            return self.hammingWeight(n>>1) + int(n&1)
