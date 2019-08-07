class Solution:
    def defangIPaddr(self, address: str) -> str: 
        defanged = ""
        for i, k in enumerate(address):
            if k == '.':
                defanged += "[.]"
            else:
                defanged += k
        return defanged
