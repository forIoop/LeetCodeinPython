
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                return [left,right]
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
        return -1
