class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    #     class Solution(object):
    # def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        
        """
        def powerOfThree(n):
            if n == 0:
                return False
            if n/3 == 1 or n == 1:
                return True
            if n%3 != 0:
                return False
            
            
            return powerOfThree(n/3)
        return powerOfThree(n)
        
        
        