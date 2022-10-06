from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0 
        output = []
        right  = left + len(p)
        
        
        
        while right <= len(s)-1:
        # for i in range(len(s) - len(p) + 1):
            right  = left + len(p)
            temp = s[left:right]
            if self.compareChar(temp , p):
                output.append(left)                
            left += 1
            
        return output
    def compareChar(self, temp, p):
        if Counter(temp) == Counter(p):
            return True 
        return False
        