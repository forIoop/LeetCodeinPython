# Sort the strings
def is_permutation(str1, str2):
    # Sort string one and string two
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    #Now compare lengths of the sorted strings
    if len(sorted_str1) != len(sorted_str2):
        return False
    return True
 
print(is_permutation("dadyeets", "dadyeet"))

# O(nlogn) time | O(n) space
