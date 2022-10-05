class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        if len(s) == 1 and s in vowels:
            return 1

        left, right = 0,k
        countVowel = 0

        for i in s[left:right]:
            if i in vowels:
                countVowel += 1
        left += 1
        right += 1
        last = countVowel
        while right <= len(s):
            temp = s[left:right]
            if s[left - 1] in vowels:
                last -= 1
            if s[right-1] in vowels:
                last += 1
            countVowel = max(last, countVowel)
            right += 1
            left += 1
        return countVowel