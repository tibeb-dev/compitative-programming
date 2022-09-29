class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == "+":
                x = stk.pop()
                y = stk.pop()
                j= int(x) + int(y) 
                stk.append(j)
            elif i == "-":
                x = stk.pop()
                y = stk.pop()
                j= int(y) - int(x) 
                stk.append(j)
            elif i == "*":
                x = stk.pop()
                y = stk.pop()
                j= int(y) * int(x) 
                stk.append(j)
            elif i == "/":
                x = stk.pop()
                y = stk.pop()
                j= int(y) / int(x) 
                j = math.trunc(j)
                stk.append(str(j))
            else:
                stk.append(i)
        return stk[0]