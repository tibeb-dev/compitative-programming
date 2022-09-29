from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = Counter(nums)
        new = new.most_common()
        
        out = []
        for i in range(k):
            out.append(new[i][0])
        return out