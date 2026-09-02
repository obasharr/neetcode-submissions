class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        self.reversedList = {}
        self.seen = {}
        self.result = []

        for word in words:
            for c in word:
                self.reversedList[c] = []

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    self.reversedList[word2[j]].append(word1[j])
                    break

        for c in self.reversedList:
            if not self.dfs(c):
                return ""

        if len(self.result) < len(self.reversedList):
            return ""

        return "".join(self.result)

    def dfs(self, c):
        if c in self.seen:
            return self.seen[c]

        self.seen[c] = False

        for neighbor in self.reversedList[c]:
            if not self.dfs(neighbor):
                return False
            
        self.seen[c] = True
        self.result.append(c)

        return True

