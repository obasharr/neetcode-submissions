class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False
    
    def contains_key(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    
    def set_end(self):
        self.is_end = True

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)

        node.set_end()

    def search_prefix(self, word: str):
        node = self.root
        
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None

        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None
        