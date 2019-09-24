class Solution:
    def getSum(self, a: int, b: int) -> int:
        #Need to conv to binary
        carry = 0
        while b != 0:
            #converts both a and b to binary, then applies AND table comparing each of their bits
            carry = a & b
            #also converts a and b to binary, then applies XOR table comparing each of their bits
            a = a ^ b
            #left shifting carry until it goes to zero, else pops the left most bit and shift
            b = carry << 1
        #returns a if no more carry
        return a
            
