#write a function to find longest common prefix of a string amongst any array of strings

def longestCommonPrefix(strs):

    #returns nothing if not in string array
    if not strs:
        return ""

    #min function gets string number alphabetically ordered first
    first = min(strs)

    #iterates through our first  picked string
    for i in range(len(first)):
        #comparing our first string to other strings in our array
        for s in strs:
          #when the indeces of the compared strings are not equal
          if s[i] != first[i]:
            #returns all indeces leading to our i value to get common value
            #assumes these strings have a prefix else return nothing
            return first[:i] if i > 0 else ''

    return first


print(longestCommonPrefix(["abc","aaa","aab"]))
