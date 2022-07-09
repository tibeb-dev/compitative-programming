class Solution(object):
    def sortColors(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(a)):
            for j in range(len(a)-1):
                if (a[j] > a[j+1]):
                    a[j] , a[j+1] = a[j+1] ,a[j]
        return a