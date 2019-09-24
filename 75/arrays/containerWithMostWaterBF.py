class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = float("-inf")
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                minimum = min(height[i],height[j])
                maximum = max(maximum, minimum * (j-i)) 
        return maximum
