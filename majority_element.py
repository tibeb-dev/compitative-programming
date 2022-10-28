class Solution:
    # def majorityElement(self, nums):
    #     majority_count = len(nums)//2
    #     for num in nums:
    #         count = sum(1 for elem in nums if elem == num)
    #         if count > majority_count:
    #             return num
            
            
    def majorityElement(self, nums):
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol