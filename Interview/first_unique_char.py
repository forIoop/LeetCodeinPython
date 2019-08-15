class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        else:
            ht = dict()
            for letter in s:
                ht[letter] = ht.get(letter,0) + 1
            
            for key in ht:
                if ht[key] == 1:  
                    return s.index(key)
            return -1
