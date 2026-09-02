class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)

        allComboDict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                newWord = word[:i] + "*" + word[i + 1:]
                allComboDict[newWord].append(word)

        queue = deque()

        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            word, level = queue.popleft()
            for i in range(L):
                newWord = word[:i] + "*" + word[i + 1:]

                for adjWord in allComboDict[newWord]:
                    if adjWord == endWord:
                        return level + 1 
                    if adjWord not in visited:
                        visited.add(adjWord)
                        queue.append((adjWord, level + 1))

        return 0
