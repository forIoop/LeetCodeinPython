class Solution:
    def maxProduct(self, nums: List[int]) -> int:

    #we need to keep track of our min and max product to determine which one to use
    curr_max_product = nums[0]
    prev_max_product = nums[0]
    prev_min_product = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        # need these for cases where next element is positive and negative
        curr_max_product = max(prev_max_product*nums[i], prev_min_product*nums[i], nums[i])
        curr_min_product = min(prev_max_product*nums[i], prev_min_product*nums[i], nums[i])
        #Global max, using kadane's algo to build up to current
        ans = max(ans, curr_max_product)
        #Update prev counters to reflect current product
        prev_max_product = curr_max_product
        prev_min_product = curr_max_product
    return ans
