class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        res = []
        for i in range(n):
		    cur_max = max(A[0:n-i])
            j = 0
            while A[j] != cur_max:
                j += 1
            # should reverse j+1 elements
            A[:j+1] = reversed(A[:j+1])
            res.append(j+1)
            # reverse all
            A[:n-i] = reversed(A[:n-i])
            res.append(n-i)
	    return res
    
    
#     [3,2,4,1]   [4,]