class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        left, right = 0, len(nums) - 1
        count = 0
        while(left < right):
            # print(nums[left], nums[right])
            j = nums[left] + nums[right]
            if j == k:
                count += 1
                right -= 1
                left += 1
            elif j < k:
                left += 1
            elif j > k:
                right -= 1
        return count