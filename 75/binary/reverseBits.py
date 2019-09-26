class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        #Iterate through max width of binary rep
        for i in xrange(32):
            #shift answer left one
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
    
#     So, in our example, I'm gonna show only first 5 right bits, since other bits are 0.
# answer = 0, in binary: 00000000000000000000000000000000
# answer << 1 is 00000000000000000000000000000000, n & 1 is 00000000000000000000000000000001
# after + operation answer is 00000000000000000000000000000001

# answer = 1, in binary: 00000000000000000000000000000001
# answer << 1 is 00000000000000000000000000000010, n & 1 is 00000000000000000000000000000001
# after + operation answer is 00000000000000000000000000000011

# answer = 3, in binary: 00000000000000000000000000000011
# answer << 1 is 00000000000000000000000000000110, n & 1 is 00000000000000000000000000000000
# after + operation answer is 00000000000000000000000000000110

# answer = 6, in binary: 00000000000000000000000000000110
# answer << 1 is 00000000000000000000000000001100, n & 1 is 00000000000000000000000000000000
# after + operation answer is 00000000000000000000000000001100

# answer = 12, in binary: 00000000000000000000000000001100
# answer << 1 is 00000000000000000000000000011000, n & 1 is 000
