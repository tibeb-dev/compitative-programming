class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        level = -1 
        result = 0
        
        for x in sorted(nums):
            if level < x:
                level = x
            else:
                level += 1
                result += level - x
                
        
        return result