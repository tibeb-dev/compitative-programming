class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mul = [1] * n 
        postfix_mul = [1] * n 
        ans = [1] * n 
        
        for i in range(1,n):
            prefix_mul[i] = prefix_mul[i - 1] * nums[i-1]
            
        for i in range(n-2 ,-1 , -1):
            postfix_mul[i] = postfix_mul[i + 1] * nums[i+1]
            
        for i in range(n):
            ans[i] = prefix_mul[i] * postfix_mul[i]
        return ans