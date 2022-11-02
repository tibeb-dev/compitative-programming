class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        attempts, stack = k, []
        
        for digit in num:
            while stack and digit < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(digit)
        
        out = "".join(stack[0:len(num)-k]).lstrip("0")
        return "0" if out == "" else out 
    
    
    "1432219"
    