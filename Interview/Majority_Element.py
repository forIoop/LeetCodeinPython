class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        ht = dict()
        for i in range(len(nums)):
            ht[nums[i]] = ht.get(nums[i],0) + 1
        
        for key in ht:
            if ht[key] == max(ht.values()):
                return key
            
       
