# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack,needle):

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return - 1

haystack = "Will you be able to find the needle in this long haystack sentence?"
needle = "te"
print("Haystack: Will you be able to find the needle in this long haystack sentence?")
print("Needle: te")
print("The index of the needle in the haystack is: ")
print(strStr(haystack,needle))
