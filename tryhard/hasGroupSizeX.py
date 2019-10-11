class Solution(object):
    import collections
    def hasGroupsSizeX(self, deck):
    
        cardCount = collections.Counter(deck)
        
        minCard = min(cardCount.values())
        if minCard < 2:
            return False
        for i in range(2, minCard+1):
            if all( val % i == 0 for val in cardCount.values()):
                return True
        return False
