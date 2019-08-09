class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        counter = 1
        i = 1
        while i < len(S):
            counter += 1 if S[i] == "(" else -1
            if counter != 0:
                result.append(S[i])
            else:
                counter = 1
                i += 1
            i += 1
        return "".join(result)
