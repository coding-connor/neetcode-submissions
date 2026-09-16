class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # less brute force 
        seen = {} # number , index 
        for i in range(len(nums)):
            looking_at = nums[i]
            difference = target - looking_at
            if difference in seen:
                return [seen[difference], i]            
            seen[looking_at] = i