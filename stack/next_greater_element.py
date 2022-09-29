class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        out = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2) - 1:
                        result.append(-1)
                    else:
                        for k in nums2[j:]:
                            if k > nums2[j]:
                                result.append(k)
                                break
                        else:
                            result.append(-1)
                   
        return result
                    
                    
        