class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        i = 0
        j= len(nums) - 1
        while i < j:
            t = nums[i] + nums[j]
            if t == k:
                count += 1
                j-= 1
                i += 1
            elif t > k:
                j -= 1
                
            else:
                i += 1
        return count