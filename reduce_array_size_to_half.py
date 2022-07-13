from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        nums = Counter(arr)
        k = nums.most_common()
        n = len(arr) // 2
        size = 0
        for j, i in enumerate(k):
            size += i[1]
            if size >= n:
                return j + 1