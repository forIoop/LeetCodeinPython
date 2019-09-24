class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        #Binary search to find min element
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        
        while low < high:
            #This is the deflection point where the array is rotated checks for dip
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            #Need to check where the array deflects
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        return nums[mid]
        
#O(n) time | O(1) space
