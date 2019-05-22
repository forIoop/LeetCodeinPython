#Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#given nums = [3,2,2,3] should return 2, first two values are 2 and 2
def remove_element(nums,val):
    i = 0

    for j in range(len(nums)):
        if (nums[j] != val):
            nums[i] = nums[j]
            i = i + 1

    return i

nums = [2,3,4,4,4,5,6,7,8]

print("array before removing element 4: ")
print(nums)
print("New array length: ")
print(remove_element(nums,4))
print("array after removing element 4: ")
print(nums)

