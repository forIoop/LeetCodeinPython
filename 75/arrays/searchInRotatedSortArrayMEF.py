class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
    
        
        #binary search algo, we need to find the dip and readjust
        while low <= high:
            mid = (low + high) // 2
            #if target is found at mid
            if nums[mid] == target:
                return mid
        
            #checks which side of array to look at
            if nums[low] <= nums[mid]:
                #if target is within low mid range
                if nums[low] <= target <= nums[mid]:
                    #adjust high pointer
                    high = mid - 1
                else:
                    #adjust low pointer
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
#O(log(n)) time | O(1) space
