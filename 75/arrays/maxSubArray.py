class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Set current and global to default 1st element
        max_current = max_global = A[0]
        
        for i in range(1,len(nums)-1):
            #current_max is the max between that element and previous current_max
            max_current = max(A[i],max_current + A[i])
            # now we need to store and ultimate global max
            if max_current > max_global
                max_global = max_current
        return max_global
    # O(n) time | O(1) space
