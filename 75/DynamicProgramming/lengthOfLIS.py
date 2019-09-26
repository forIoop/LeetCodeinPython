class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #simplt return 0 if no numbers to compare
        if len(nums) == 0:
            return 0
        
        #max length array initalized to best answer of 1
        maxLength = [1 for i in range(len(nums))]
        maxSoFar = 1
        #two pointers to find max and append to maxLenght array
        for i in range(1,len(nums)):
            for j in range(0,i):
                #if array is ascending compute the max between maxLength[i] and maxLength[j+1]
                if nums[i] > nums[j]:
                    maxLength[i] = max(maxLength[i],maxLength[j]+1)
            maxSoFar = max(maxSoFar, maxLength[i])
        return maxSoFar
