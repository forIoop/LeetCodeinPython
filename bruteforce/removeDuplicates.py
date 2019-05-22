#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return
#the new length
 
def remove_duplicates(nums):
    #index to compare
    i = 0

    for j in range(1,len(nums)):
        #if not duplicate adjust index pointer and copy the value of j into that updated pointer

        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]

    return i + 1

nums = [5,5,7,9]
print("nums array before rmoving duplicates:")
print(nums)

print("nums array after removing duplicates:")
print(remove_duplicates(nums))
print(nums)
