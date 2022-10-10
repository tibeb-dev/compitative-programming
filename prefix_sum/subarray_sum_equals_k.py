class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            count=0
            p=0
            d={0:1}

            for num in nums:
                p = p + num

                if p-k in d:
                    count = count + d[p-k]

                if p not in d:
                    d[p] = 1
                else:
                    d[p] = d[p]+1

            return count