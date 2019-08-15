class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = int((len(nums) * (len(nums)+1))/2)
        
        for num in nums:
            missing -= num
        return missing
        
