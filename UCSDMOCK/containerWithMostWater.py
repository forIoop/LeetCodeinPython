# Brute force O(n^2) solution O(1) space
def containerMostWater(heights):
    maximum = float("-inf")
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            minimumHeight = min(heights[i],heights[j])
            maximum = max(maximum, minimumHeight * (j - i))
    return maximum


# One pass solution O(n) O(1) space 
def containerMostWater2(heights):
    maximum = float("-inf")
    left = 0
    right = len(heights) - 1
    while left < right:
        minimumHeight = min(heights[left],heights[right])
        maximum = max(maximum,minimumHeight * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -=1
    return maximum


print(containerMostWater([1,8,6,2,5,4,8,3,7]))
print(containerMostWater2([1,8,6,2,5,4,8,3,7]))
