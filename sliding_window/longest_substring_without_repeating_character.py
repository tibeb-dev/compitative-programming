class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        nonReapting = []
        for i in s:
            if i  not in nonReapting:
                nonReapting.append(i)
            else:
                counter = max(counter , len(nonReapting))
                while nonReapting[0] != i:
                    nonReapting.pop(0)

                nonReapting.pop(0)
                nonReapting.append(i)
        
        return max(counter , len(nonReapting))

                