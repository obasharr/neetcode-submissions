class Solution:
    def isValid(self, s: str) -> bool:
        mapped_brackets = {')': '(','}': '{',']': '['}

        stack = []

        for c in s:
            if c not in mapped_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != mapped_brackets[c]:
                    return False
                
        return len(stack) == 0
