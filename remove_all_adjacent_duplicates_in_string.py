class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for i in s:
            if len(ans) > 0:
                if i == ans[-1]:
                    ans.pop()
                else:
                    ans.append(i)
            else:
                ans.append(i)
        return ''.join(ans)