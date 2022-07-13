class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = ""
        
        for i in s:
            if i == ")":
                cur = ""
                while(stk[-1] != "("):
                    cur += stk[-1]
                    stk = stk[:-1]
                stk = stk[:-1]
                cur1 = "".join(cur)
                stk += cur1
            else:
                stk += i
        return stk