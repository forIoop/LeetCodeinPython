class Solution:
    def isHappy(self, n: int) -> bool:

        ht = dict()
        while n:
            if 1 in ht:
                return True
            if n in ht:
                return False
            ht[n] = 0
            tmp = 0
            while n:
                tmp += (n%10) ** 2
                n //= 10
            n = tmp
