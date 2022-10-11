class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        result = sys.maxsize
        left = 0
        target_sum = 0
        n = len(nums)
        
        for i in range(n):
            target_sum += nums[i]
            while (target_sum >= target):
                result = min(result , i+1-left)
                target_sum -=nums[left]
                left += 1
        
        return result if result != sys.maxsize else 0
        