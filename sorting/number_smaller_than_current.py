class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        result = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j :
                    continue
                else:
                    if nums[i]>nums[j]:
                        count +=1
            result[i] = count
            count = 0
        return result
        