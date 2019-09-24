class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        if a & b == 0:
            return 0
        return getSum(a ^ b, (a & b)<<1)
