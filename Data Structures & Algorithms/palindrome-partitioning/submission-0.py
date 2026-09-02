class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(result, [], s, 0)
        return result

    def backtrack(self, result: List[List[str]], current: List[str], s: str, start: int):
        if start == len(s): 
            result.append(current.copy())
            return 
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                current.append(s[start:end + 1])
                self.backtrack(result, current, s, end + 1)
                current.pop()
    
    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True