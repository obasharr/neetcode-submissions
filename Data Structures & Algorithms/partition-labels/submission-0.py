class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurance = [0] * 26

        for i in range(len(s)):
            lastOccurance[ord(s[i]) - ord('a')] = i

        result = []
        partitionEnd = 0
        partitionStart = 0

        for i in range(len(s)):
            partitionEnd = max(partitionEnd, lastOccurance[ord(s[i]) - ord('a')])

            if i == partitionEnd:
                result.append(partitionEnd - partitionStart + 1)
                partitionStart = i + 1

        return result