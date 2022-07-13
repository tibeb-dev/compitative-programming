class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        
        left = 1
        right = len(piles) - 1
        maxval = 0
        
        while(left < right):
            maxval += piles[left]
            left += 2
            right -= 1
        return maxval