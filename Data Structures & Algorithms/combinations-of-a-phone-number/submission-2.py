class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digitToLetters = ["", "", "abc", "def", "ghi", 
        "jkl", "mno", "pqrs", "tuv", "wxyz"]

        combinations = []
        if not digits:
            return combinations
        
        self.backtrack(combinations, digits, "", 0)

        return combinations

    def backtrack(self, combinations: List[str], digits: str, currentCombination: str, index: int):
        if index == len(digits):
            combinations.append(currentCombination)
            return 
        letters = self.digitToLetters[int(digits[index])]
        for letter in letters:
            self.backtrack(combinations, digits, currentCombination + letter, index + 1)

