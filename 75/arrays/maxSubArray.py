class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = A[0]
        for i in range(1,len(nums)-1):
            max_current = max(A[i],max_current + A[i])
            if max_current > max_global
                max_global = max_current
        return max_global
