class Solution(object):
    def climbStairs(self, n): 
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        #[1,2,3,5,8]
        res[0] , res[1] = 1,2
        for i in xrange(2,n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
    
    # O(n) time and O(n) space
