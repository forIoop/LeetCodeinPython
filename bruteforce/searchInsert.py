#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
  length = len(nums)
  left = 0
  right = length - 1

  while left <= right:
    mid = (left + right) // 2
    if target > nums[mid]:
      if mid == length - 1:
        return length
      if target < nums[mid+1]:
        return mid + 1
      else:
        left = mid + 1

    elif target < nums[mid]:
      if mid == 0:
        return 0
      if target > nums[mid-1]:
        return mid
      else:
        right = mid - 1
    else:
      return mid


nums = [3,5,6,7]
target = 1
print(searchInsert(nums,target))
