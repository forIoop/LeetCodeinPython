# Upper Bound: O(n^2n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space

def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + ar ray[i + 1:]
            newPermutatation = currentPermutation + array[i]
            permutationHelper(newArray, newPermutation, permutations)

