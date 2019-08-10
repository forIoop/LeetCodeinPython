class Solution:
    def reverseString(self, s: List[str]) -> None:
        last_idx = len(s) - 1
        for i in range(len(s)):
            s.insert(i,s.pop(last_idx))
