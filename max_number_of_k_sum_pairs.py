class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i] + nums[j] == k :
                    nums.pop(i)
                    nums.pop(j)
                    count += 1
                