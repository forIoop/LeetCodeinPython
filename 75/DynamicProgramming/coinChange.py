class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        numOfCoins = [float("inf") for coinAmount in range(amount + 1)]
        numOfCoins[0] = 0

        for denom in coins:
            for coinAmount in range(len(numOfCoins)):
                if denom <= coinAmount:
                    numOfCoins[coinAmount] = min(numOfCoins[coinAmount], 1 + numOfCoins[coinAmount - denom])
        return numOfCoins[amount] if numOfCoins[amount] != float("inf") else -1
                    
                    
