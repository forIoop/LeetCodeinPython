class Solution:
    def countBits(self, num: int) -> List[int]:
        sol = []
        #iterate through every number leading up to num
        for i in range(num+1):
            count = 0
            #while there still are potential 1 bits
            while i != 0:
                #case where we encounter a 1, increment count
                if i % 2 == 1:
                    count += 1
                #shift bits to the right one, ex: 8 in binary is 1000 so shifting it would be 0100
                i = i >> 1
            sol.append(count)
            return sol
