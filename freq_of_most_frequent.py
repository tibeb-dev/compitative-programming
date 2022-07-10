class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        j = 0
        ans , cum = 1,nums[j]
        for i in range(1,len(nums)):
            while nums[i]*(i-j)-cum>k:
                cum -= nums[j]
                j += 1
            cum += nums[i]
            ans = max(ans, i-j+1)
        return ans
    
