class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        result = []
        for i in range(len(nums)):
            result.append(int(nums[i]))
        print("integer version" ,result)
        result.sort()
        print("sorted version",result)
        return str(result[-k])