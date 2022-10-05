class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left , right = 0 , k
        counter = 0
        temp = arr[left:right]
        # for j in range(k):
        #     total += temp[j]
        total = sum(temp)
        average = total / k
        if average >= threshold:
            counter += 1
        left += 1
        right += 1    
        
        while right <= len(arr):
            total -= temp[0]
            temp = arr[left:right]
            total += temp[k-1]
            average = total / k
            if average >= threshold:
                counter += 1
            left += 1
            right += 1
        return counter
            