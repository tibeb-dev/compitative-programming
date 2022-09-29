class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                result.append(item)
            elif item == ')':
                if len(result) == 0:
                    return False
                else:
                    if result[-1]== "(":
                        result.pop()
                    else:
                        return False
            elif item == '}':
                if len(result) == 0:
                    return False
                else:
                    if result[-1]== "{":
                        result.pop()
                    else:
                        return False
            elif item == "]":
                if len(result) == 0:
                    return False
                else:
                    if result[-1]== "[":
                        result.pop()
                    else:
                        return False
        if len(result) == 0:
            return True

