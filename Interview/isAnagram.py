class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            
            letters = []
            for i in range(len(s)):
                letters.append(s[i])
            
            for j in range(len(t)):
                if t[j] in letters:
                    letters.remove(t[j])
                else:
                    return False
            return True
