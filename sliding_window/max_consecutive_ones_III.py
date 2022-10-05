class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        result = zeroCount = 0
        i, j = 0, 0 
        while  j < len(A):
            if A[j] == 0:
                if zeroCount < K:
                    zeroCount += 1
                else:
                    result = max(result, j - i)
                    while A[i] != 0:
                        i += 1
                    i += 1
            j += 1
        result = max(result, j - i)
        return result