class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_stack = []
        min_stack = []
        last_popped = -1
        res = 0
        for i in range(len(nums)):
            while max_stack and nums[i]+limit < nums[max_stack[0]]:
                last_popped = max(last_popped, max_stack.pop(0))
            while min_stack and nums[i]-limit > nums[min_stack[0]]:
                last_popped = max(last_popped, min_stack.pop(0))
            res = max(res, i-last_popped)
            while max_stack and nums[max_stack[-1]] <= nums[i]:
                max_stack.pop()
            max_stack.append(i)
            while min_stack and nums[min_stack[-1]] >= nums[i]:
                min_stack.pop()
            min_stack.append(i)
        return res
