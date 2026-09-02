class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return chr(258)

        seperator = chr(257)

        return seperator.join(strs)

    def decode(self, s: str) -> List[str]:

        if s == chr(258):
            return []


        seperator = chr(257)

        return s.split(seperator)

