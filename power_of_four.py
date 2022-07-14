class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        """
        :type n: int
        :rtype: bool
        
        """
        def powerOfFour(n):
            if n == 0:
                return False
            if n/4 == 1 or n == 1:
                return True
            if n%4 != 0:
                return False
            
            
            return powerOfFour(n/4)
        return powerOfFour(n)
        
        
        