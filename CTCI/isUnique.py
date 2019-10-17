def isunique(str):
    # If length of string is greater than ascii value for unique chars, return false
    if len(str) > 128:
        return False

    # Sets every ascii value to false initially
    arr = [False] * 128
    for char in str:
        index = ord(char) #Ascii value for that character
        # if in boolean array then we know it was visited before
        if arr[index]:
            return False
        #if it is not in the array then set it to visited
        arr[index] = True
    # return true if it passes and no arr[index] overlap
    return True

# O(1) time because once we traverse over 128 elements we just return false so constant
# O(1) space since we are storing a constant space of 128 elements
