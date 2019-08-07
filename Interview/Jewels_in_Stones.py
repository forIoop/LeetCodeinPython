class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ht = dict()
        count = 0
        for i,k in enumerate(J):
            ht[i] = k
        
        for j,letter in enumerate(S):
            if letter in ht.values():
                count += 1
        return count
