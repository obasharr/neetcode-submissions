class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        
        for i in range(len(s)):
            len1 = self.checkPalindrome(s, i, i)
            len2 = self.checkPalindrome(s, i, i + 1)
            len_max = max(len1, len2)

            if len_max > right - left:
                left = i - (len_max - 1) // 2
                right = i + len_max // 2

        return s[left:right + 1]

    def checkPalindrome(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
