class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        out = []
        left = 0
        right = len(nums) - 1
        while(left<right):
            out.append(nums[left] + nums[right])
            left += 1
            right -= 1
        return max(out)